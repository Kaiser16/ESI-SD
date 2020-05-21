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

    print("Habitación "+str(id))
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
    if(res.text == ""):
        print("Los datos no se introdujeron correctamente")
    else:
        print("Creada habitación "+res.text)

def modificarHabitacion():
    id = input("Identificador de la habitación: ")
    op = -1
    res = requests.get("http://localhost:8080/buscarHabitacion/"+id)
    if(res.text == ""):
        print("La habitación buscada no existe")
    else:
        imprimirHabitacion(res.json())
        while(op != "0"):
            print("|MODIFICAR HABITACIÓN "+id+"|")
            print("1.Modificar plazas")
            print("2.Modificar equipamiento")
            print("3.Modificar estado de ocupacion")
            print("0.Salir") 
            op = input("\nOpcion: ")
            if(op == "1"):
                plazas = input("Introduce el numero de plazas: ")
                res = requests.put("http://localhost:8080/modificarHabitacion/"+id,json={"plazas": plazas})
            elif(op == "2"):
                equipamiento = input("Introduce el equipamiento separado por (,): ")
                res = requests.put("http://localhost:8080/modificarHabitacion/"+id,json={"equipamiento": equipamiento.split(",")})
            elif(op == "3"):
                ocupada = input("Ocupada(s/n): ")
                if(ocupada == "s"):
                    bOcupada = True
                else:
                    bOcupada = False
                res = requests.put("http://localhost:8080/modificarHabitacion/"+id,json={"ocupada": bOcupada})
            if(op == "1" or op == "2" or op == "3"):
                if(res.text == ""):
                    print("La modificacion introducida es incorrecta")
                else:
                    print("Habitación modificada "+res.text+"\n")

def listaHabitaciones():
    res = requests.get("http://localhost:8080/listaHabitaciones")
    if(res.text == "{}"):
        print("No existen habitaciones")
    else:
        print("|LISTA DE HABITACIONES|")
        print(res.text)
        for valor in res.json():
            imprimirHabitacion(res.json()[valor])

def buscarHabitacion():
    id = input("Identificador de la habitacion: ")
    print("|HABITACIÓN "+id+"|")
    res = requests.get("http://localhost:8080/buscarHabitacion/"+id)
    if(res.text == ""):
        print("La habitación buscada no existe")
    else:
        imprimirHabitacion(res.json())

def eliminarHabitacion():
    id = input("Identificador de la habitacion: ")
    res = requests.put("http://localhost:8080/eliminarHabitacion/"+id)
    if(res.text == ""):
        print("La habitación a eliminar no existe")
    else:
        print("La habitacion "+res.text+" ha sido eliminada")

def habitacionesDesocupadas():
    res = requests.get('http://localhost:8080/habitaciones/Desocupadas')
    print("|LISTA DE HABITACIONES DESOCUPADAS|")
    for valor in res.json():
        imprimirHabitacion(valor)

def habitacionesOcupadas():
    res = requests.get('http://localhost:8080/habitaciones/Ocupadas')
    print("|LISTA DE HABITACIONES OCUPADAS|")
    for valor in res.json():
        imprimirHabitacion(valor)

while(op != "0"):
    print("|API HOTEL|")
    print("1. Dar de alta habitación")
    print("2. Modificar habitación")
    print("3. Lista de habitaciones")
    print("4. Buscar habitación")
    print('5. Habitaciones desocupadas')
    print('6. Habitaciones ocupadas')
    print("7. Eliminar habitacion")
    print("0. Salir")
    op = input("\nOpción: ")
    if(op == "1"):
        altaHabitacion()
    elif(op == "2"):
        modificarHabitacion()
    elif(op == "3"):
        listaHabitaciones()
    elif(op == "4"):
        buscarHabitacion()
    elif(op == '5'):
        habitacionesDesocupadas()
    elif(op == '6'):
        habitacionesOcupadas()
    elif(op == "7"):
        eliminarHabitacion()