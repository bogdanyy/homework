import socket

HOST = "127.0.0.1"
PORT = 5000

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #server 1-setevoe vzaimod,
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
srv.bind((HOST, PORT))
srv.listen(20)  # 20 razmer ocheredi
try:
	client, addr = srv.accept() #vozvraschaet client i ego adres
	print("connecting with" + addr[0] + ":" + (addr[1]))
	for index in range(1,10):
		data = client.recv(2048)  # razmer dannih,kot mi prochitaem
		print(data.decode)("utf-8")
		if not data:  #esli net data app stop
			break
		result = f"{data}\n{addr}\n"
		client.send(data)
except Exception as e:
	print(e)
finally:""
srv.close()
