import socket
from networkingConstants import *
import struct
import pickle
import cv2


def interceptMaster():
   while True:
       try:
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.connect((host, port))
           return s, s.makefile('wb')
       except:
           print("socket error reconnecting")
           time.sleep(5)





while True:
    TCPClientSocket, Conn = interceptMaster()
    data = b""
    payload_size = struct.calcsize(">L")
    print("payload_size: {}".format(payload_size))
    while True:
        while len(data) < payload_size:
            print("Recv: {}".format(len(data)))
            data +=  TCPClientSocket.recv(bufferSize)
        print("Done Recv: {}".format(len(data)))
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        print("msg_size: {}".format(msg_size))
        while len(data) < msg_size:
            data += TCPClientSocket.recv(bufferSize)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        try:
            frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            print("Broadcasting")
            # broadcast_socket.sendto(frame_data, (UDP_IP, UDP_PORT))
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            resized = cv2.resize(frame, (64,64), interpolation = cv2.INTER_AREA)
            cv2.imwrite('frame.jpg', resized)
            cv2.imshow('frame', resized)
            cv2.waitKey(1000)
        except:
            print("Problem Broadcasting")




