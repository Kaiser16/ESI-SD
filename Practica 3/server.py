import json
from bottle import run, request, response, get, post, put

class Room:
    def __init__(self, id, plazas, equipamiento, ocupada):
        self.id = id
        self.plazas = plazas
        self.equipamiento = equipamiento
        self.ocupada = ocupada

def guardar(data,filename):
    f = open(filename,'w')
    json.dump(data,f,indent=4)
    f.close()

def cargar(filename):
    try:
        f = open(filename)
        datos = json.load(f)
        f.close()
    except:
        datos = {}
        datos['habitaciones'] = {}
        datos['maxId'] = 0
    return datos

@post('/altaHabitacion')
def alta_habitacion():

    bd = cargar('bd.json')

    habitaciones = bd['habitaciones']
    
    data = request.json

    plazas = data.get('plazas')
    if(not plazas.isnumeric()):
        return ""
    equipamiento = data.get('equipamiento')
    ocupada = data.get('ocupada')
    
    habitacion = Room(bd['maxId'],plazas,equipamiento,ocupada)

    habitaciones[bd['maxId']] = habitacion.__dict__
    bd['maxId'] += 1

    response.headers['Content-Type'] = 'application/json'

    guardar(bd,'bd.json')
    return json.dumps(habitacion.__dict__)

@put('/modificarHabitacion/<identificador>')
def modificar_habitacion(identificador):
    bd = cargar('bd.json')

    habitacion = bd['habitaciones'][identificador]

    data = request.json
    plazas = data.get('plazas') 
    equipamiento = data.get('equipamiento')
    ocupada = data.get('ocupada')

    if(plazas != None):
        if(not plazas.isnumeric()):
            return ""
        else:
            habitacion['plazas'] = plazas
    if(equipamiento != None):
        habitacion['equipamiento'] = equipamiento
    if(ocupada != None):
        habitacion['ocupada'] = ocupada

    guardar(bd,'bd.json')

    return habitacion

@get('/buscarHabitacion/<identificador>')
def buscar_habitacion(identificador):
    try:
        bd = cargar('bd.json')
        return bd['habitaciones'][identificador]
    except:
        return ""

@get('/listaHabitaciones')
def lista_habitaciones():
    bd = cargar('bd.json')
    return bd['habitaciones']

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)