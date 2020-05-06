import socket
import os

HOST = 'localhost'
PORT = 1025

Sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensaje = "Soy el cliente"

Sudp.sendto(mensaje.encode(),(HOST,PORT))

Sudp.close()