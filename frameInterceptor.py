import socket
from networkingConstants import *
import struct
import pickle
import cv2

def interceptMaster():
    msgFromClient = "balans_rocks"
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = (MASTER_IP, MASTER_UDP_PORT )
# Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    return UDPClientSocket

while True:
    UDPClientSocket = interceptMaster()
    data = b""
    payload_size = struct.calcsize(">L")
    print("payload_size: {}".format(payload_size))
    while True:
        while len(data) < payload_size:
            print("Recv: {}".format(len(data)))
            data +=  UDPClientSocket.recvfrom(bufferSize)
        print("Done Recv: {}".format(len(data)))
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        print("msg_size: {}".format(msg_size))
        while len(data) < msg_size:
            data += UDPClientSocket.recvfrom(bufferSize)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        print("Broadcasting")
        # broadcast_socket.sendto(frame_data, (UDP_IP, UDP_PORT))
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)





