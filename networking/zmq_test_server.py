#!/usr/bin/env python

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://0.0.0.0:5000")

while True:
	msg = socket.recv()
	print msg
	socket.send("hallo, " + msg)
