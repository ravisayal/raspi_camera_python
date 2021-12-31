from picamera import PiCamera
import time
from datetime import datetime

camera = PiCamera()
time.sleep(2)

camera.resolution = (800, 600)
camera.vflip = True
camera.contrast = 10
camera.image_effect = "watercolor"

date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = "./img_" + date_time + ".jpg"

camera.capture(file_name)
print("Done.")