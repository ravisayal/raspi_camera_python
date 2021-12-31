from picamera import PiCamera
import time
from datetime import datetime

camera = PiCamera()
time.sleep(2)

camera.resolution = (800, 600)
camera.vflip = True
camera.contrast = 10


date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
print("Date and Time:",date_time)

file_name = "./video_" + date_time + ".h264"
print("Start recording...")
camera.start_recording(file_name)
camera.wait_recording(5)
camera.stop_recording()
print("Done.")