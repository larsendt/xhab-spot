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
    return sp.Popen("roscore", close_fds=True, stdout=sp.PIPE, stderr=sp.PIPE)


def stop_roscore(roscore_proc):
    if roscore_proc:
        proc = psutil.Process(roscore_proc.pid)
        roscore_proc.kill()
        roscore_proc.wait()
        print "Killed ROS Core:", proc
    else:
        for proc in psutil.process_iter():
            for item in proc.cmdline:
                if "roscore" in item or "rosmaster" in item:
                    os.kill(proc.pid, signal.SIGKILL)
                    print "Killed ROS Core:", proc



ROS_NODES = ["battery_node.py",
             "camera_controller.py",
             #"data_archiver.py",
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

if __name__ == "__main__":
    roscore_proc = start_roscore()
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
        print "Done"



