import cv2
from threading import Thread
import time

class WebcamVideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        loop_time = time.time()
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

            # check if 10 seconds have passed
            if time.time() - loop_time >= 10:
                self.stream.release()  # release the current video stream
                self.stream = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # open a new video stream
                loop_time = time.time()  # reset the loop time

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
