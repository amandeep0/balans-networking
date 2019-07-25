import socket
import queue
import threading

import time
from networkingConstants import *

class FrameBroadCaster():
    def __init__(self, bufferSize = bufferSize, port = MASTER_RELAY_PORTS):
        self.connected_addresses = {}
        self.bufferSize = bufferSize
        self.localIP =  "0.0.0.0"
        self.localPorts = ports
        self.TCPServerSocket = []
        #asyncio.gather(self.listenInterceptors(self.UDPServerSocket))
    def listenInterceptors(self):
        while True:
            print("Waiting For Interception")
            bytesAddressPair = self.UDPServerSocket.recvfrom(self.bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]
            print("Intercepted: ", address)
            if address not in self.connected_addresses:
                self.connected_addresses[address] = 1
    def initiateConnection(self):
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPServerSocket.bind((self.localIP, self.localPort))
        print("Binded to Socket")
        return UDPServerSocket

    def sendData(self, bytesToSend):
        addresses = self.connected_addresses.keys()
        for address in addresses:
            print("Sending to: ", address)
            self.UDPServerSocket.sendto(bytesToSend, address)





# Bind to address and ip


#
# print("UDP server up and listening")
#
# # Listen for incoming datagrams
#
# while (True):
#     bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
#
#     message = bytesAddressPair[0]
#
#     address = bytesAddressPair[1]
#
#     clientMsg = "Message from Client:{}".format(message)
#     clientIP = "Client IP Address:{}".format(address)
#
#     print(clientMsg)
#     print(clientIP)
#
#     # Sending a reply to client
#
#     UDPServerSocket.sendto(bytesToSend, address)
