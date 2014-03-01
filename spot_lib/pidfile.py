#!/usr/bin/env python

import psutil
import os
import time
import json

PID_DIR = "/home/xhab/pidfiles"

def pid_filename(class_name, pid):
    return os.path.join(PID_DIR, class_name + "." + str(pid) + ".pid")

def create_pidfile(class_name):
    timestamp = time.time()
    pid = os.getpid()
    obj = {"pid":pid, "time":timestamp, "name":class_name}

    if not os.path.exists(PID_DIR):
        os.makedirs(PID_DIR)

    pid_fname = pid_filename(class_name, pid)
    with open(pid_fname, "w") as f:
        json.dump(obj, f)

    return pid_fname


def get_pids(active):
    pids = []
    for fname in os.listdir(PID_DIR):
        with open(fname, "r") as f:
            obj = json.load(f)

        try:
            proc = psutil.Process(obj["pid"])
            if active:
                pids.append((obj["pid"], obj["name"]))
        except psutil.NoSuchProcess:
            if not active:
                pids.append((obj["pid"], obj["name"]))

    return pids


def get_active_class_pids(class_name):
    active_pids = get_pids(True)
    return filter(lambda x: x[1] == class_name, active_pids)


def get_pidinfo(class_name, pid):
    pid_fname = pid_filename(class_name, pid)
    if os.path.exists(pid_fname):
        with open(pid_fname, "r") as f:
            return json.load(f)
    else:
        return None


def cleanup_dead_pids():
    for fname in get_pids(False):
        os.remove(fname)

