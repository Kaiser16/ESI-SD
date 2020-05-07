from bottle import get, post, request, route, run, template

@get('/')
def altaHabitacion():
    return '''
    <form action="/" method="post">
        Numero de Plazas <input name="nPlazas" type="number" required/>
        <br><br>
        Equipamiento (Separados por ',') <input name="equipamiento" type="textarea" required/>
        <br><br>
        Ocupada <input type="checkbox" name="ocupada" value=0>
        <br><br>
        <input type="submit" value="Enviar Habitación"/>
    </form>
    '''

@post('/')
def hacerAltaHabitacion():
    nPlazas = request.forms.get('nPlazas')
    listaEquipamiento = request.forms.get('equipamiento').split(",")
    ocupada = request.forms.get('ocupada')
    a = template("{{nPlazas}}\n", nPlazas = nPlazas)
    for equipamiento in listaEquipamiento:
        a = a + template("{{equipamiento}}\n", equipamiento = equipamiento)
    if(ocupada=="0"):
        a = a + " ocupado"

    
    return a

run(host='localhost', port=8080)