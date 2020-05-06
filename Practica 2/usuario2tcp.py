import socket
import os

HOST = 'localhost'
PORT = 1025

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
	mensaje = input("Enviar: ")

	s.send(mensaje.encode())

	mensaje = s.recv(1024)

	print("RECIBIDO: ["+mensaje.decode()+"] del servidor")

s.close()