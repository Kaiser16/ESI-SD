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
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.servidor.bind(miDireccion)
    
    def direccion(self):
        return self.direccion
    
    def servidor(self):
        return self.servidor

class ClienteEnvio(Thread):
    def __init__(self, cliente):
        self.servidor = cliente.servidor
        self.destino = cliente.destino
        Thread.__init__(self)
    
    def run(self):
        salir = False
        nombre = None
        while not salir:
            mensaje = input()
            if mensaje == '!salir':
                salir = True
                mensaje += nombre
            elif not nombre:
                mensaje = nombre = '[' + mensaje + ']'
            elif mensaje != '!ayuda':
                mensaje = nombre + ' ' + mensaje
            self.servidor.sendto(codificar(mensaje), self.destino)

class ClienteRecepcion(Thread):
    def __init__(self, cliente):
        self.servidor = cliente.servidor
        self.salir = False;
        Thread.__init__(self)
    
    def intentarSalida(self):
        self.salir = True;
    
    def run(self):
        while not self.salir:
            mensaje, direccion = self.servidor.recvfrom(4096)
            mensaje = decodificar(mensaje)
            if mensaje == 'cerrarServer':
                print("[Servidor] Se ha cerrado el servidor, por favor introduce !salir para salir.")
                self.salir = True
            if mensaje not in ['!salir', '!ayuda', 'cerrarServer']:
                print(mensaje)


puerto = int(input("Introduce el puerto: "))
try:
    c = Cliente(('localhost', puerto), ('localhost', 8888))
except OSError:
    print("Dirección en uso.")
    exit()
envio = ClienteEnvio(c)
recepcion = ClienteRecepcion(c)
print("Inserta tu nombre de usuario: ", end="")
try:
    envio.start()
    recepcion.start()
    envio.join()
    recepcion.intentarSalida()
    recepcion.join()
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")