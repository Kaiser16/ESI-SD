import json, string
from server import Room, guardar, cargar

habitaciones = dict()
habitaciones["0"] = Room("0","12","tele",False)
habitaciones["1"] = Room("1","16","tele",False)
print(habitaciones)
