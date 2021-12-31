from picamera import PiCamera
import time
camera = PiCamera()
time.sleep(2)
camera.resolution = (1280, 720)
camera.vflip = True
camera.contrast = 10
camera.image_effect = "watercolor"
file_name = "./img_" + str(time.time()) + ".jpg"
camera.capture(file_name)
print("Done.")