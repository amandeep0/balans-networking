import cv2
import io
import socket
import struct
import time
import pickle
import zlib

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

 # initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))



  # allow the camera to warmup
time.sleep(0.1)




host  = '167.71.166.191'
port  = 5006
print("Begin")
def connect():
   while True:
       try:
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.connect((host, port))
           return s, s.makefile('wb')
       except:
           print("socket error reconnecting")
           time.sleep(5)

client_socket, connection = connect()
img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

for frame in camera.capture_continuous(rawCapture, format="bgr",  use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the $
        # and occupied/unoccupied text
        image = frame.array

        # show the frame
        try:
        	result, image = cv2.imencode('.jpg', image, encode_param)
        	data = pickle.dumps(image, 0)
        	size = len(data)

        	rawCapture.truncate(0)
               
        	print("{}: {}".format(img_counter, size))
        	client_socket.sendall(struct.pack(">L", size) + data)
        	img_counter += 	1
        except  socket.error as e:
         # Handle disconnection -- close & reopen socket etc.
        	client_socket, connection = connect()
        	rawCapture.truncate(0)             







