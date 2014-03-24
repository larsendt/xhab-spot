#!/usr/bin/python

import cv
import sys, time, datetime

#put the device number here. Can be found by running 'ls /dev/video*' command.
#if only one camera is connected to pc, then it is set to 0
#in case of laptop, device 0 corresponds to integrated webcam
cam_device = 0
capture = cv.CreateCameraCapture(cam_device)
if not capture:
   print "Error opening Device"
   sys.exit()

def capture_stream(path):
        frame = cv.QueryFrame(capture)
        stamp = time.time()
        if frame is None:
               print "no frame"
               sys.exit()
        cv.Flip(frame, None, 1)
        # the image extension can be changed to desired format. replace .ppm with .jpg/.jpeg/.png etc
        image_name = "image_"+`stamp`+".ppm"
        cv.SaveImage(path+image_name, frame)
        return image_name

# the following while loop is for testing purpose. 
# uncomment the while loop to see how the capture_stream() can be used.

#while 1:
#        image = capture_stream("/home/xhab/xhab-spot/camera/")
#        prefix,stamp = image.split("_", 1)
#        stamp,postfix = stamp.split(".ppm", 1)
#        print stamp+"  "+`datetime.datetime.fromtimestamp(float(stamp)).strftime('%Y-%m-%d_%H:%M:%S')`
        #the delay mentioned below can be varied
        #for now keeping this, so that less images will be generated in the given amount of time
#        key = cv.WaitKey(50)
#        if key == 27: # press ESC key to exit
#           break

