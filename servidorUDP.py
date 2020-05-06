import socket
import os

HOST = 'localhost'
PORT = 1025


sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sudp.bind((HOST,PORT))

print("Me quedo a la espera")
mensaje = sudp.recvfrom(1024)

print("Recibido el mensaje: "+str(mensaje))
sudp.close()