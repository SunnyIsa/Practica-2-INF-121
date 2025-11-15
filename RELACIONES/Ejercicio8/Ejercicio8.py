#Ejercicio 8. La entrada universitaria requiere un sistema para gestionar las diversas
#fraternidades, bailarines y facultades que participaran este año. Para ello se pide que
#pueda se pueda ver a los bailarines y a que fraternidad y facultad pertenecen, además
#conocer al encargado de cada fraternidad, ver las edades de los participantes y verificar
#que no estén en 2 o más fraternidades. Cada vez que haya un nuevo integrante debe de
#ser registrado tomando sus datos personales, la facultad y fraternidad a la que pertenecen
#respectivamente.#a) Identifica las clases y atributos necesarios para resolver el problema
class Fraternidad:
	def __init__(self,nombre,encargado):
		self.nombre=nombre
		self.encargado=Encargado(encargado.nombre,encargado.edad,self.nombre)
		self.participantes=[]
	def agregar(self,participante):
		if participante.fraternidad == "":
			participante.fraternidad=self.nombre
			self.participantes.append(participante)
		else:
			print(participante.nombre,"ya esta en la fraternidad",participante.fraternidad)
	def mostrarP(self):
		for i in range(len(self.participantes)):
			print(self.participantes[i])
	def __str__(self):
			s=self.encargado.__str__()
			return "Fraternidad: "+self.nombre+" "+s
class Facultad:
	def __init__(self,nombre):
		self.nombre=nombre
		self.participantes=[]
	def agregar(self,participante):
		participante.facultad=self.nombre
		self.participantes.append(participante)
	def mostrarP(self):
		for i in range(len(self.participantes)):
			print(self.participantes[i])

class Persona:
	def __init__(self,nombre,edad):
		self.nombre=nombre
		self.edad=edad
class Participante (Persona):
	def __init__(self,nombre="",edad=0,facultad="",fraternidad=""):
		super().__init__(nombre,edad)
		self.facultad=facultad
		self.fraternidad=fraternidad
	def __str__(self):
		return "Nombre: {} | Edad {} | Facultad: {} | Fraternidad: {}".format(self.nombre,self.edad,self.facultad,self.fraternidad)
class Encargado(Persona):
	def __init__(self,nombre,edad,fraternidad):
		super().__init__(nombre,edad)
		self.fratAsignada=fraternidad
	def __str__(self):
		return "Encargado: {} | Edad {} | Fraternidad asignada: {}".format(self.nombre,self.edad,self.fratAsignada)
#b) Instancia al menos 5 participantes de los cuales 2 fraternidades con sus respectivos encargados y 2 facultades.
#c) Resuelve lo que pide el cliente	
enc1 = Persona("Carlos", 35)
enc2 = Persona("Ana", 30)

ing = Facultad("Ingeniería")
der = Facultad("Derecho")

andinos = Fraternidad("Los Andinos", enc1)
tupac = Fraternidad("Tupac Katari", enc2)

p1 = Participante("Juan", 20)
p2 = Participante("María", 19)
p3 = Participante("Luis", 22)
p4 = Participante("Elena", 21)
p5 = Participante("Pablo", 23) 
ing.agregar(p1)
ing.agregar(p2)
ing.agregar(p3)
der.agregar(p4)
der.agregar(p5)
andinos.agregar(p1)
andinos.agregar(p2)
andinos.agregar(p3)
tupac.agregar(p3)
tupac.agregar(p4)
tupac.agregar(p5)
print(andinos)
andinos.mostrarP()
print(tupac)
tupac.mostrarP()
