import json
import requests

class Room:
    def __init__(self, id, plazas, equipamiento, ocupada):
        self.id = id
        self.plazas = plazas
        self.equipamiento = equipamiento
        self.ocupada = ocupada

def guardar(data,filename):
    f = open(filename,'w')
    json.dump(data,f,indent=4)

def cargar(filename):
    try:
        jsonf = open(filename)
        datos = json.load(jsonf)
    except:
        datos = {}
        datos['nHabitaciones'] = 0
        datos['maxId'] = 0
    return datos