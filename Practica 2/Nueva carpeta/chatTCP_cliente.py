import socket
import sys
from threading import Thread

def codificar(mensaje):
    return mensaje.encode('utf-8')

def decodificar(mensaje):
    return mensaje.decode('utf-8')

class Cliente:
    def __init__(self, miDireccion, otroDireccion):
        self.direccion = miDireccion
        self.destino = otroDireccion
        self.servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.servidor.connect(otroDireccion)
        self.servidor.settimeout(0.1)

    
    def direccion(self):
        return self.direccion
    
    def servidor(self):
        return self.servidor

class ClienteEnvio(Thread):
    def __init__(self, cliente, recpSalir):
        self.servidor = cliente.servidor
        self.destino = cliente.destino
        self.recpSalir = recpSalir
        Thread.__init__(self)
    
    def run(self):
        salir = False
        while not salir:
            mensaje = input("[Yo] ")
            if mensaje == '!salir':
                salir = True;
                self.recpSalir = True
            else:
                self.servidor.send(codificar(mensaje))


class ClienteRecepcion(Thread):
    def __init__(self, cliente):
        self.servidor = cliente.servidor
        self.salir = False;
        Thread.__init__(self)
    
    def intentarSalida(self):
        self.salir = True;
    
    def run(self):
        while not self.salir:
            try:
                mensaje = self.servidor.recv(1024).decode()
                print("-> "+mensaje)
            except:
                pass

puerto = int(input("Introduce el puerto: "))
try:
    c = Cliente(('localhost', puerto), ('localhost', 8888))
except OSError:
    print("Dirección en uso.")
    exit()
recepcion = ClienteRecepcion(c)
envio = ClienteEnvio(c,recepcion.salir)
try:
    envio.start()
    recepcion.start()
    envio.join()
    recepcion.intentarSalida()
    recepcion.join()
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")