import socket
import sys
from threading import Thread

def codificar(mensaje):
    return mensaje.encode('utf-8')

def decodificar(mensaje):
    return mensaje.decode('utf-8')

class Servidor(Thread):
    def __init__(self, direccion):
        self.clientes = list()
        self.destino = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.destino.bind(direccion)
        self.destino.settimeout(1)
        self.direccion = direccion
        self.actual = 0
        try:
            fich = open('registro')
            self.actual = int(fich.read()) + 1
            fich.close()
        except:
            print('Hubo un error que no permite cargar el número del último registro.')
            print('Se va a tomar el primer registro como 0, por lo que si ya había otro')
            print('con dicho valor, se va a sobreescribir.')
            val = input('¿Deseas continuar (Si/No)? ')
            if not (val == 'Si' or val == 'si'):
                print('Se ha cancelado la carga.')
                print('Escribe en el fichero registro el número del último registro.')
                exit()
        try:
            fich = open('ayuda')
            self.ayuda = '[Servidor] ' + fich.read()
            fich.close()
        except:
            print("Hubo un error que no permite cargar el sistema de ayuda.")
            print("¿Quizá no existe el fichero de ayuda?");
            self.ayuda = '[Servidor] No hay ayuda disponible.'
        self.salir = False
        Thread.__init__(self)
    
    def destino(self):
        return destino

    def intentarSalida(self):
        self.salir = True

    def run(self):
        registro = ""
        while not self.salir:
            try:
                mensaje, dir = self.destino.recvfrom(4096)
                mensaje = decodificar(mensaje)
                if dir not in self.clientes and dir != self.direccion:
                    self.clientes.append(dir)
                    mensaje = '[Servidor] Se ha unido ' + mensaje + '.'
                    print(mensaje)
                if mensaje.startswith('!salir'):
                    mensaje = '[Servidor] Se ha cerrado la conexión con ' + mensaje[6:] + '.'
                    self.destino.sendto(codificar('[Servidor] Has salido del chat.'), dir)
                    print(mensaje)
                    self.clientes.remove(dir)
                if mensaje == '!ayuda':
                    self.destino.sendto(codificar(self.ayuda), dir)
                else:
                    for cliente in self.clientes:
                        if cliente != dir:
                            self.destino.sendto(codificar(mensaje), cliente)
                    if mensaje != 'cerrarServer':
                        registro += mensaje + '\n'
            except:
                pass
        fich = open('registro_' + str(self.actual), 'w')
        fich.write(registro)
        fich.close()
        fich = open('registro', 'w')
        fich.write(str(self.actual))
        fich.close()
        
class Emisor(Thread):
    def __init__(self, direccion, servidor):
        self.servidor = servidor
        self.objetivo = direccion
        Thread.__init__(self)
    
    def run(self):
        salir = False
        while not salir:
            mensaje = input()
            if mensaje == '!salir':
                salir = True
                mensaje = 'cerrarServer'
            else:
                mensaje = '[Servidor] ' + mensaje
            self.servidor.sendto(codificar(mensaje), self.objetivo)

def ejecutarServidor():
    direccion = ('127.0.0.1', 8888)
    s = Servidor(direccion)
    e = Emisor(direccion, s.destino)
    e.start()
    s.start()
    e.join()
    s.intentarSalida()
    s.join()

ejecutarServidor()