from mySocket import mySocket
import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5001
# print(pickle.dumps(pkt))
udpsocket=mySocket(socket.AF_INET,socket.SOCK_DGRAM)
udpsocket.custom_create(UDP_IP,UDP_PORT)
udpsocket.recv_from(4096)
print('closing server...')
udpsocket.close()