#!/usr/bin/env python

import zmq
import hashlib

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://0.0.0.0:5000")

print "listening"
while True:
	msg = socket.recv()
	print "got: '" + msg + "'"
	if msg == "req:filename":
		socket.send("filename:datafile.bin")
		print "sent filename: datafile.bin"
	elif msg == "req:sha1sum":
		with open("datafile.bin", "r") as f:
			data = f.read()
			m = hashlib.sha1()
			m.update(data)
			socket.send("sha1sum:" + m.hexdigest())
			print "sent sha1sum: " + m.hexdigest()
	elif msg == "req:contents":
		with open("datafile.bin", "r") as f:
			data = f.read()
			socket.send("contents:" + data)
			print "sent contents: %d bytes" % len(data)
	else:
		print "unknown request"
		socket.send("unknown request")
