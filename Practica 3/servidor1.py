class ServidorHotel:
	class Habitacion:
		def __init__(self,identificador,nPlazas,equipamiento,ocupada)
			self.identificador = identificador
			self.nPlazas = nPlazas
			self.equipamiento = equipamiento
			self.ocupada = ocupada

	def __init__(self):
		self.habitaciones = list()

	def altaHabitacion(self,nPlazas,equipamiento,id):
		h = self.Habitacion(id,nPlazas,equipamiento,False)
		self.habitaciones.append(h)

	def modificarPlazas(self,nPlazas,id):
		self.habitaciones[id].nPlazas = nPlazas

	def modificarEquipamiento(self,nuevoEquipamiento,id):
		self.habitaciones[id].equipamiento = nuevoEquipamiento

	def modificarOcupada(self,ocupada,id):
		self.habitaciones[id].ocupada = ocupada

	def listaHabitaciones(self):
		return self.habitaciones

	def verHabitacion(self,id):
		return self.habitaciones[id]

	def habitacionesOcupadas(self):
		l = list()
		for habitacion in self.habitaciones:
			if(habitacion.ocupada == True)
				l.append(self.habitaciones)
		return l

	def habitacionesDesocupadas(self):
		l = list()
		for habitacion in self.habitaciones:
			if(habitacion.ocupada == False)
				l.append(self.habitaciones)
		return l