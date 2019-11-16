import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
camera.start_preview()
camera.annotate_text = 'Hello world!'
time.sleep(2)
# Take a picture including the annotation
camera.capture('my_image.jpg')
camera.close()


##########################################################import picamera
##import time
##import itertools
##import picamera
##s = "Hello World! This is text overlay"
##
##camera = picamera.PiCamera()
##camera.resolution = (640, 480)
##camera.framerate = 24
##camera.start_preview()
##camera.annotate_text = ' ' * 31
##for c in itertools.cycle(s):
##    camera.annotate_text = camera.annotate_text[1:31] + c
##    time.sleep(0.1)
##sleep(1)
##camera.close()
