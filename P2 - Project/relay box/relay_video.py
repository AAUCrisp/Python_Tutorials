from djitellopy import tello
import cv2

tello = tello.Tello()

def video_stream():
    tello.streamon()

    while True:
        img = tello.get_frame_read().frame # get the 
        #img = cv2.resize(img, (360,240))
        cv2.imshow("Live Stream", img)
        cv2.waitKey(1)
