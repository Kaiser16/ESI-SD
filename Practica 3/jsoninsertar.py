from room import Room, cargar,guardar
import json

dbfile = 'datos.json'

datos = cargar(dbfile)
hab = Room(datos['maxId'],3,["ventilador","lavadora"],False)
datos[str(datos['maxId'])] = hab.__dict__
datos['nHabitaciones'] += 1
datos['maxId'] += 1
guardar(datos,dbfile)