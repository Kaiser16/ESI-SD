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
        self.destino = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.destino.bind(direccion)
        self.destino.listen(5)
        self.destino.settimeout(0.1)
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
        while not self.salir:
            for conexion in self.clientes:
                try:
                    conexion.settimeout(0.1)
                    mensaje = conexion.recv(1024).decode()
                except:
                    continue
                print("mensaje:" + mensaje)
                for cliente in self.clientes:
                    if cliente != conexion and cliente != self.destino:
                        mensaje = "\n"+str(conexion.getsockname())+" "+mensaje
                        cliente.send(codificar(mensaje))


class Aceptar(Thread):
    def __init__(self, servidor, lista):
        self.servidor = servidor
        self.lista = lista
        self.salir = False
        Thread.__init__(self)

    def run(self):
        while not self.salir:
            try:
                con,dir = self.servidor.accept()
                print(str(con)+" Conectado")
                self.lista.append(con)
            except:
                pass


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
        self.destino.close()


def ejecutarServidor():
    direccion = ('127.0.0.1', 8888)
    s = Servidor(direccion)
    e = Emisor(direccion, s.destino)
    a = Aceptar(s.destino, s.clientes)
    e.start()
    s.start()
    a.start()
    e.join()
    s.intentarSalida()
    s.join()
    a.join()

ejecutarServidor()