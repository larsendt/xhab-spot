#!/usr/bin/env python

import subprocess as sp
import time
import sys
import os
import signal
import psutil
from threading  import Thread
from Queue import Queue, Empty

SERVICE_DIR = "service_files/"

if not os.path.exists(SERVICE_DIR):
    os.makedirs(SERVICE_DIR)

class Service(object):
    def __init__(self, cmd):
        self.cmd = cmd.split(" ")
        self.cmdline = cmd
        self.proc = None
        self.stdout_queue = None
        self.stderr_queue = None
        self.stdout_thread = None
        self.stderr_thread = None
        self.stdout = []
        self.stderr = []
        self.is_alive = False

    def run(self):
        print self.cmdline
        self.proc = sp.Popen(self.cmd, stdout=sp.PIPE, stderr=sp.PIPE, close_fds=True)
        self.stdout_queue = Queue()
        self.stdout_thread = Thread(target=self.enqueue_output, args=(self.proc.stdout, self.stdout_queue))
        self.stdout_thread.daemon = True
        self.stdout_thread.start()
        self.stderr_queue = Queue()
        self.stderr_thread = Thread(target=self.enqueue_output, args=(self.proc.stderr, self.stderr_queue))
        self.stderr_thread.daemon = True
        self.stderr_thread.start()
        self.is_alive = True

    def kill(self):
        try:
            self.proc.kill()
            self.proc.wait()
        except:
            print "Service '%s' is already dead" % self.cmdline
        self.is_alive = False

    def enqueue_output(self, out, queue):
        for line in iter(out.readline, b''):
            queue.put(line)
        out.close()

    def update(self):
        try:
            while True:
                stdout = self.stdout_queue.get_nowait()
                self.stdout.append(stdout)
                with open(SERVICE_DIR + self.cmd[2] + ".stdout.txt", "a") as f:
                    f.write(stdout)
        except Empty:
            pass

        try:
            while True:
                stderr = self.stderr_queue.get_nowait()
                self.stderr.append(stderr)
                with open(SERVICE_DIR + self.cmd[2] + ".stderr.txt", "a") as f:
                    f.write(stderr)
        except Empty:
            pass

        ret = self.proc.poll()
        if ret != None and self.is_alive:
            print "Service '%s' exited with return code %d!" % (self.cmdline, ret)
            print ""
            print "==============================================="
            print "".join(self.stderr)
            print "==============================================="
            print ""
            self.stdout_thread.join()
            self.stderr_thread.join()
            self.is_alive = False
            print "Marked service as not alive"


def start_roscore():
    for proc in psutil.process_iter():
        for item in proc.cmdline:
            if "rosmaster" in item or "roscore" in item:
                print "ROS Core is already running"
                return None
    print "Starting ROS Core"
    return sp.Popen("roscore", close_fds=True, stdout=sp.PIPE, stderr=sp.PIPE)


def stop_roscore(roscore_proc):
    if roscore_proc:
        proc = psutil.Process(roscore_proc.pid)
        print "Killing ROS Core:", proc
        roscore_proc.kill()
        roscore_proc.wait()
    else:
        for proc in psutil.process_iter():
            for item in proc.cmdline:
                if "roscore" in item or "rosmaster" in item:
                    print "Killing ROS Core:", proc
                    os.kill(proc.pid, signal.SIGKILL)


def start_lcd_driver():
    print "Starting LCD driver"
    proc = sp.Popen(["python", "/home/xhab/xhab-spot/spot_lib/lcd_menu.py"], close_fds=True, stdout=sp.PIPE, stderr=sp.PIPE)
    return proc

def stop_lcd_driver(proc):
    print "Killing lcd interface:", psutil.Process(proc.pid)
    proc.kill()
    proc.wait()
    for p in psutil.process_iter():
        for item in p.cmdline:
            if "interrupt" in item:
                print "killling interrupt process", p
                os.kill(p.pid, signal.SIGKILL)


ROS_NODES = ["battery_node.py",
             "camera_controller.py",
             "data_archiver.py",
             "door_controller.py",
             "ec_sensor.py",
             "fan_controller.py",
             "humidity_sensor.py",
             "lcd_interface.py",
             "light_controller.py",
             "ph_sensor.py",
             "pump_controller.py",
             "water_level_sensor.py",
             "rotation_controller.py"]

CMDS = map(lambda x: "rosrun xhab_spot " + x, ROS_NODES)
SERVICES = map(lambda x: Service(x), CMDS)

def check_already_running():
    otherproc = None
    for proc in psutil.process_iter():
        if "launch_spot.py" in " ".join(proc.cmdline) and proc.name == "python":
            if proc.pid != os.getpid():
                otherproc = proc
                break

    if otherproc is None:
        return
    
    print "Found another SPOT process:", proc.pid
    print "Self is:", os.getpid()
    print "Type 'y' to shut down other process, 'n' to exit"
    inp = ""
    while inp != "y" and inp != "n":
        inp = raw_input("[y/n] ")

    if inp[0] == "y":
        print "Terminating other process..."
        os.kill(proc.pid, signal.SIGINT)
        time.sleep(3)
    else:
        print "Exiting"
        sys.exit(0)


def main():
    check_already_running()
    roscore_proc = start_roscore()
    lcd_proc = start_lcd_driver()
    print "Launching %d services" % len(SERVICES)
    map(lambda x: x.run(), SERVICES)
    print "Monitoring services"
    try:
        while True:
            time.sleep(1)
            map(lambda x: x.update(), SERVICES)
    except KeyboardInterrupt:
        print "Terminating all services"
        map(lambda x: x.kill(), SERVICES)
        stop_roscore(roscore_proc)
        stop_lcd_driver(lcd_proc)
        print "Done"


if __name__ == "__main__":
    main()
