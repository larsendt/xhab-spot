#!/usr/bin/env python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
print "connecting"
socket.connect("tcp://192.168.55.1:5000")

print "sending"
for i in range(10):
    msg = "msg %s" % i
    socket.send(msg)
    print "Sending", msg
    msg_in = socket.recv()
