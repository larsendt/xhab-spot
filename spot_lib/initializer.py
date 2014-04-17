#!/usr/bin/env python

import lockfile
import json
import os

LOCKPATH = "/home/xhab/data/initializer.lock"
DATAPATH = "/home/xhab/data/initializer.json"

def put_variable(key, value):
    lock = lockfile.FileLock(LOCKPATH)
    try:
        lock.acquire(timeout=60)
    except LockTimeout:
        print "Lock file was taken for more than 60 seconds, breaking it!"
        lock.break_lock()

    try:
        obj = {}
        if os.path.exists(DATAPATH):
            with open(DATAPATH, "r") as f:
                obj = json.load(f)

        obj[key] = value
        with open(DATAPATH, "w") as f:
            json.dump(obj, f)
    except:
        return False
    finally:
        lock.release()

def get_variable(key, default=None):
    obj = {}
    if os.path.exists(DATAPATH):
        with open(DATAPATH, "r") as f:
            try:
                obj = json.load(f)
            except:
                return default
    
    return obj.get(key, default)

if __name__ == "__main__":
    put_variable("asdf", "hjkl")
    print get_variable("asdf")
    print get_variable("bbbb")
