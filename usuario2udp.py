import socket
import os

HOST = 'localhost'
PORTR = 1026
PORTE = 1025

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((HOST,PORTR))

while True:
	print("Enviar: ", end = '')
	mensaje = input()
	cliente.sendto(mensaje.encode(),(HOST,PORTE))
	
	print("Me quedo a la espera")
	mensaje = servidor.recvfrom(1024)
	print("Recibido: "+str(mensaje))

cliente.close()