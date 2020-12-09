from picamera import PiCamera
from time import sleep
import threading as th


class CameraModule:
    
    def __init__ (self):
        self.cam = PiCamera()
        
    def show(self, seconds=5):
        self.cam.start_preview()
        sleep(seconds)
        self.cam.stop_preview()
        
        
        # the following functions create a loop which will break if you hit enter
        # this way I can show a live video stream until I want to physically stop it
        # keep_going = True
        # def key_capture_thread():
        #     global keep_going
        #     input()
        #     keep_going = False
        
        # def do_stuff():
        #     th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
        #     while keep_going:
        #         sleep(1)

        # if seconds == 0:
        #     self.cam.start_preview()
        #     do_stuff()
        #     self.cam.stop_preview()

        # else:
        #     self.cam.start_preview()
        #     sleep(seconds)
        #     self.cam.stop_preview()
