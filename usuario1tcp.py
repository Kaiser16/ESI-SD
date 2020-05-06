import socket

HOST = 'localhost'
PORT = 1025

socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socketServidor.bind((HOST,PORT))
socketServidor.listen(1)

s_cliente, addr = socketServidor.accept()
while mensaje != "/apagar":
	print("Nos quedamos a la espera...")
	mensaje = s_cliente.recv(1024)

	print("Recibo:["+mensaje.decode()+"] del cliente con la direccion"+str(addr))

	mensaje = input("Enviar: ")

	s_cliente.send(mensaje.encode())

s_cliente.close()
socketServidor.close()