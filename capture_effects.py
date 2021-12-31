from picamera import PiCamera, Color
import time
from datetime import datetime

camera = PiCamera()
time.sleep(2)

camera.resolution = (800, 600)
camera.vflip = True
camera.contrast = 10

camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    time.sleep(1)
    print ("Now using Effect: %s" % effect)
    camera.annotate_text = "Effect: %s" % effect
    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = "./img_" + date_time + "_" + effect +".jpg"
    camera.capture(file_name)
    time.sleep(1)

