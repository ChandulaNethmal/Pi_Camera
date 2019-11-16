from time import sleep
from picamera import PiCamera
import sys
import time

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(3)
T=True
i=0
while (T==True):
    try:
        
        #timestr=time.strftime("%Y%m%d-%H%M%S")
        #trig=input("Press '+' to capture an image:" )
        sleep(2)
        timestr=time.strftime("%Y%m%d-%H%M%S")
        camera.capture(timestr + '.jpg')
        
    except KeyboardInterrupt:
        print("Exiting from camera......")
        camera.close()
        T=False
        sys.exit(0)

    
