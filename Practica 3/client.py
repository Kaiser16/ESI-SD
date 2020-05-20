import json
import requests

op = -1

def imprimirHabitacion(habitacion):
    id = habitacion['id']
    plazas = habitacion['plazas']
    equipamiento = habitacion['equipamiento']
    n = len(equipamiento)
    cadequip = equipamiento[0]
    if(n > 1):
        i = 1
        while(i < n):
            if(i < n-1):
                cadequip += ", "+equipamiento[i]
            else:
                cadequip += " y "+equipamiento[i]
            i += 1
    ocupada = habitacion['ocupada']

    print("Habitacion "+str(id))
    print("\t- "+plazas+" plazas")
    print("\t- Equipamiento: "+cadequip)
    if(ocupada):
        print("\t- Ocupada")
    else:
        print("\t- Libre")

def altaHabitacion():
    plazas = input("Introduce el numero de plazas: ")
    equipamiento = input("Introduce el equipamiento separado por (,): ")
    ocupada = input("Ocupada(s/n): ")
    if(ocupada == "s"):
        bOcupada = True
    else:
        bOcupada = False
    res = requests.post("http://localhost:8080/altaHabitacion",json={"plazas": plazas, "equipamiento": equipamiento.split(","), "ocupada": bOcupada})
    print("Creada habitacion "+res.text)

def modificarHabitacion():
    id = input("Identificador de la habitacion: ")
    op = -1
    while(op != "0"):
        print("|MODIFICAR HABITACION "+id+"|")
        print("1.Modificar plazas")
        print("2.Modificar equipamiento")
        print("3.Modificar estado de ocupacion")
        print("0.Salir") 
        op = input("\nOpcion: ")
        if(op == "1"):
            plazas = input("Introduce el numero de plazas: ")
            res = requests.put("http://localhost:8080/modificarHabitacion/"+id,json={"plazas": plazas})
        if(op == "2"):
            equipamiento = input("Introduce el equipamiento separado por (,): ")
            res = requests.put("http://localhost:8080/modificarHabitacion/"+id,json={"equipamiento": equipamiento.split(",")})
        if(op == "3"):
            ocupada = input("Ocupada(s/n): ")
            if(ocupada == "s"):
                bOcupada = True
            else:
                bOcupada = False
            res = requests.put("http://localhost:8080/modificarHabitacion/"+id,json={"ocupada": bOcupada})
        if(op == "1" or op == "2" or op == "3"):
            print("Habitacion modificada "+res.text+"\n")

def listaHabitaciones():
    res = requests.get("http://localhost:8080/listaHabitaciones")
    print("|LISTA DE HABITACIONES|")
    for valor in res.json():
        imprimirHabitacion(res.json()[valor])

def buscarHabitacion():
    id = input("Identificador de la habitacion: ")
    print("|HABITACION "+id+"|")
    res = requests.get("http://localhost:8080/buscarHabitacion/"+id)
    imprimirHabitacion(res.json())

while(op != "0"):
    print("|API HOTEL|")
    print("1. Dar de alta habitacion")
    print("2. Modificar habitacion")
    print("3. Lista de habitaciones")
    print("4. Buscar habitacion")
    print("0. Salir")
    op = input("\nOpcion: ")
    if(op == "1"):
        altaHabitacion()
    if(op == "2"):
        modificarHabitacion()
    if(op == "3"):
        listaHabitaciones()
    if(op == "4"):
        buscarHabitacion()