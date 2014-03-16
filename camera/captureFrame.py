#!/usr/bin/python

#press ESC key to exit
#press "t" to display the time and date of frame
#pass "-timestamp" or "--t" commandline arg to store frames with timestamp name format
#if no args passed, frames are stored in serial number name format
	
import cv
import sys, time, datetime

cv.NamedWindow('video_stream')
#put the device number here. Can be found by running 'ls /dev/video*' command.
#if only one camera is connected to pc, then it is set to 0
#in case of laptop, device 0 corresponds to integrated webcam
cam_device = 0
capture = cv.CreateCameraCapture(cam_device)
if not capture:
   print "Error opening Device"
   sys.exit()

img_cnt = 0
dt = 0

def argcheck():
        if len(sys.argv) > 1:
           firstarg = str(sys.argv[1])
           return (firstarg == "-timestamp" or firstarg == "--t")
        else: return 0

def capture_stream():
        frame = cv.QueryFrame(capture)
        stamp = time.time()
        if frame is None:
                sys.exit()
        cv.Flip(frame, None, 1)
        cv.ShowImage('video_stream', frame)
        # the image extension can be changed to desired format. replace .ppm with .jpg/.jpeg/.png etc
        if argcheck():
           image = "image_"+`stamp`+".ppm"
        else:
           image = "image_"+`img_cnt`+".ppm"
        cv.SaveImage(image, frame)
        return stamp
   
while 1:
        stamp = capture_stream()
        img_cnt = img_cnt+1
        #the delay mentioned below can be varied
        #for now keeping this, so that less images will be generated in the given amount of time
        key = cv.WaitKey(50)
        if key == 27: # press ESC key to exit
           break
        elif key == 116: #press "t" to display the time and date of frame
           dt = datetime.datetime.fromtimestamp(stamp).strftime('%Y-%m-%d_%H:%M:%S')
           print dt


