import socket
import threading

import time
from networkingConstants import *

class FrameBroadCaster():
    def __init__(self, bufferSize = bufferSize, ports = MASTER_RELAY_PORTS):
        self.connected_addresses = {}
        self.bufferSize = bufferSize
        self.localIP =  "0.0.0.0"
        self.localPorts = ports
        self.TCPServerSocket = []
        #asyncio.gather(self.listenInterceptors(self.UDPServerSocket))
    
    def initiateConnection(self, port):
        print("Interceptor Listening Initiated : ", port)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print('Interceptor socket created')
        s.bind((self.localIP,port))
        print('Interceptor bind complete')
        s.listen(10)
        conn, addr=s.accept()
        print("Intercepted", port)
        self.TCPServerSocket.append((port, conn))
    
    def listenInterceptors(self):
        for port in self.localPorts:
            listenor_thread = threading.Thread(target=self.initiateConnection, args=(port, ))
            listenor_thread.start()

    def sendData(self, bytesToSend):
        connections =  self.TCPServerSocket.copy()
        if len(connections) == 0:
            print("Not Intercepted yet")
        for conn_tuple in connections:
            print("Sending to: ", conn_tuple[0])
            conn_tuple[1].sendall(bytesToSend)





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
