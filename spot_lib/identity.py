#!/usr/bin/env python

def get_spot_name():
    with open("/etc/hostname", "r") as f:
        hostname = f.read().replace("\n", "").replace("-", "")
    return hostname

if __name__ == "__main__":
    print get_spot_name()
