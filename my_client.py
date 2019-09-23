import socket
import sys
import requests


HOST = "127.0.0.1"
PORT = 5000

#def creat_soc():
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #server 1-setevoe vzaimod,
print("connect")
srv.connect((HOST,PORT))
print ("Connection success!")
#def dend_data(srv, data):
srv.send = ("hello")
data = srv.recv(2048)
print ("Received response")
srv.close()

#if __name__ == '__main__':
#	creat_soc()
	#srv = 
#	send_data(srv, "hello")






#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))
#s.send('hello') 
#data = s.recv(1000000)
#print 'received', data, len(data), 'bytes'
#s.close()
