import socket
import os
import sys

def recibir(nombre):
	s.send(nombre.encode())

	t = s.recv(1024).decode()

	tam = int(t)
	#print(tam)
	if(tam != 0):
		f = open(nombre,'wb')
		
		while (tam > 0):
			l = s.recv(1024)
			f.write(l)
			tam -= sys.getsizeof(l)
			#print(tam)
		f.close()
		print("Archivo '"+nombre+"' recibido")
	else:
		print("El archivo "+nombre+" no existe")

def enviar(nombre):
	try:
		#print(nombre)
		s.send(nombre.encode())
		f = open(nombre,'rb')

		stats = os.stat(nombre)

		tam = stats.st_size
		#print(tam)
		s.send(str(tam).encode())
		if(tam == 0):
			print("Archivo Vacio")
		else:
			l = f.read(1024)

			while (l):
				s.send(l)
				l = f.read(1024)
			print("Enviado")
		f.close()
	except IOError:
		print("El archivo "+nombre+" no existe")
		s.send(str(0).encode())

HOST = 'localhost'
PORT = 1025

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
	print("1. Lista de Archivos de Servidor")
	print("2. Descargar Archivo")
	print("3. Subir Archivo")
	print("4. Salir")
	op = int(input("Opcion: "))
	s.send(str(op).encode())
	if(op == 1):
		lista = s.recv(1024).decode()
		print("\n|LISTA DE ARCHIVOS|")
		print(lista+"\n")
	if(op == 2):
		nombre = input("Nombre: ")
		recibir(nombre)		

	if(op == 3):
		nombre = input("Nombre: ")
		enviar(nombre)
	if(op == 4):
		break;
s.close()