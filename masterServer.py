import socket
import sys
import cv2
import pickle
import numpy as np
import struct
import zlib
import time
from frameBroadcaster import *
from networkingConstants import *


def connectRasPi(HOST, PORT):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket created')
    s.bind((HOST,PORT))
    print('Socket bind complete')
    s.listen(10)
    conn,addr=s.accept()
    return (conn,addr)


def relayData(conn):
    data = b""
    payload_size = struct.calcsize(">L")
    print("payload_size: {}".format(payload_size))
    socket = FrameBroadCaster(port=MASTER_UDP_PORT)
    listenor_thread = threading.Thread(target=socket.listenInterceptors)
    listenor_thread.start()
    while True:
        while len(data) < payload_size:
            print("Recv: {}".format(len(data)))
            received_data = conn.recv(bufferSize)
            print("Relaying Received Data")
            socket.sendData(received_data)
            data += received_data
        print("Done Recv: {}".format(len(data)))
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        print("msg_size: {}".format(msg_size))
        while len(data) < msg_size:
            received_data = conn.recv(bufferSize)
            socket.sendData(received_data)
            data += received_data
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        print("Broadcasting")
        #broadcast_socket.sendto(frame_data, (UDP_IP, UDP_PORT))
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        #cv2.imwrite("feed/" + str(counter) + ".jpg",frame)
        #time.sleep(0.5)
HOST='0.0.0.0'
PORT=5006


conn, address = connectRasPi(HOST, PORT)
relayData(conn)
