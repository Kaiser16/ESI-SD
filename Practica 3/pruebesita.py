import json
from server import Room, guardar, cargar

bd = dict()

try:
    f = open('bd.json')
    bd = json.load(f)
    f.close()
except:
    datos = {}
    datos['nHabitaciones'] = 0
    datos['maxId'] = 0