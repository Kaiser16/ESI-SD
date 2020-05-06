import socket
import os
import sys
import glob

def enviar(nombre):
	try:
		f = open(nombre,'rb')

		stats = os.stat(nombre)

		tam = stats.st_size
		#print(tam)
		s_cliente.send(str(tam).encode())

		l = f.read(1024)

		while (l):
			s_cliente.send(l)
			l = f.read(1024)
		print("Enviado")
		f.close()
	except IOError:
		s_cliente.send(str(0).encode())
		print ("Error Envio")

def recibir(nombre):
	t = s_cliente.recv(1024).decode()

	tam = int(t)
	print(tam)
	if(tam != 0):
		f = open(nombre,'wb')
		
		while (tam > 0):
			l = s_cliente.recv(1024)
			f.write(l)
			tam -= sys.getsizeof(l)
			#print(tam)
		f.close()
		print("Archivo '"+nombre+"' recibido")
	else:
		print("Error Subida")

def listar():
	string = ""
	for file in glob.glob('*[!'+nombreServidor+']*'):
	    string = string+"\n-> "+file
	return string

HOST = 'localhost'
PORT = 1025
nombreServidor = "ftpserver.py"

socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketServidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socketServidor.bind((HOST,PORT))
socketServidor.listen(1)
while True:
	print("Esperando a que un usuario se conecte...")
	s_cliente, addr = socketServidor.accept()
	print("Usuario conectado")
	while True:
		print("Esperando Opcion...")
		m = s_cliente.recv(1024).decode()
		#print(m)
		op = int(m)
		if(op == 1):
			lista = listar()
			s_cliente.send(lista.encode())
		if(op == 2):
			print("Esperando peticion...")
			nombre = s_cliente.recv(1024).decode()
			if(nombre == nombreServidor):
				s_cliente.send(str(0).encode())
			else:
				enviar(nombre)
		if(op == 3):
			print("Esperando archivo...")
			nombre = s_cliente.recv(1024).decode()

			#print(nombre.decode())
			recibir(nombre)
		if(op == 4):
			break

	s_cliente.close()
socketServidor.close()