import os
import sys
import time
from datetime import datetime
from random import randint
import signal
import psutil
import socket

HOST = "127.0.0.1"
PORT = 5000
PID_FILE = "/var/run/step/demon/demon.pid"
WORK = True

def demon():

	def handler(signum, frame):
		print('Signal handler called with signal', signum)
		signal.signal(signal.SIGUSR1, handler)

	def creat_soc():
		srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #server 1-setevoe vzaimod,
		srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		srv.bind((HOST, PORT))
		srv.listen(20)  # 20 razmer ocheredi
		try:
			client, addr = srv.accept() #vozvraschaet client i ego adres
			print("connecting")
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

def start_demon():
	if os.path.isfile(PID_FILE):
		with open(PID_FILE, "r") as pid_file:
			pid = int(pid_file.readline())
			for process in psutil.process_iter():
				if process.pid == pid:
					print("Demon is working.")
				return
	pid = os.fork()
	if pid:
		with open(PID_FILE, "w") as pid_file:
			pid_file.write(f"{pid}")
		print("Demon was started.")
		print(f"Demon has pid: {pid}")
	else:
		demon()

def get_pid():
    pid = 0
    with open(PID_FILE, "r") as pid_file:
        pid = int(pid_file.readline())
    return pid

def send_signal(arg):
    keys ={"-s": lambda: os.kill(get_pid(), signal.SIGUSR1)}
    try:
        print(arg)
        keys[arg]()
    except KeyError as e:
        print(f"Key <{arg}> not found.")
    return

if __name__ == '__main__':
	 try:
		 os.mkdir(os.path.join(*os.path.split(PID_FILE)[:-1]))
	 except FileNotFoundError:
		 try:
			 os.makedirs(os.path.join(*os.path.split(PID_FILE)[:-1]))
		 except PermissionError:
			 print("WTF !!!")
			 sys.exit(1)
		 except FileExistsError:
			 pass
			 args = sys.argv[1:]
			 if len(args):
				 send_signal(args[0])
			 else:
				 start_demon()
