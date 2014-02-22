#!/usr/bin/env python

import netifaces as ni
import socket
import sys
import requests

wlan = None
for iface in ni.interfaces():
    if "wlan" in iface:
        wlan = iface

if wlan is None:
    print "No wlan interface found!"

ip = ni.ifaddresses(wlan)[2][0]['addr']
hostname = socket.gethostname()
print hostname, ":", ip

payload = {"host": hostname, "ip": ip}
url = "http://pcduino-ips.larsendt.com"
r = requests.post(url, data=payload)
print r.content
print "posted on", url
