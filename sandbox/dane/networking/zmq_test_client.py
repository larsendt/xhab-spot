#!/usr/bin/env python
import zmq
import hashlib
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
print "connecting"
socket.connect("tcp://192.168.55.1:5000")

def request_file(socket):
    socket.send("req:filename")
    fname = socket.recv()
    if not fname.startswith("filename:"):
        raise ValueError("Expected return message to start with 'filename:', instead got '%s'" % (fname[0:25]))
    else:
        fname = fname[len("filename:"):]

    socket.send("req:sha1sum")
    shasum = socket.recv()
    if not shasum.startswith("sha1sum:"):
        raise ValueError("Expected return message to start with 'sha1sum:', instead got '%s'" % (fname[0:25]))
    else:
        shasum = shasum[len("sha1sum:"):]

    socket.send("req:contents")
    contents = socket.recv()
    if not contents.startswith("contents:"):
        raise ValueError("Expected return message to start with 'contents:', instead got '%s'" % (fname[0:25]))
    else:
        contents = contents[len("contents:"):]

    m = hashlib.sha1()
    m.update(contents)
    if shasum != m.hexdigest():
        raise ValueError("Shasum mismatch!")

    return fname, contents

print "requesting file"
start = time.time()
fname, contents = request_file(socket)
stop = time.time()
print "got file %s" % fname
sz = len(contents)
print "%.1fKBps" % ((sz / (stop - start))/1000.0)

with open(fname, "w") as f:
    f.write(contents)

print "wrote", fname

