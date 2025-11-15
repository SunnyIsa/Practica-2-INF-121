#Ejercicio 6. Completa el diagrama de clases usando las relaciones que se indica, agrega además almenos 2 atributos significativos
class Producto:
	 def __init__( self, nombre, precio ) :
	 	 self.nombre = nombre
	 	 self.precio = precio
class Cosmetico(Producto):
 	 def __init__(self ,nombre, precio , marca , tipo):
 	 	 super().__init__(nombre,precio)
 	 	 self.marca=marca
 	 	 self.tipo=tipo
 	 def __str__(self):
 	 	return "Nombre: "+self.nombre+" Precio: "+str(self.precio)
class Medicamento(Producto):
	def __init__(self,nombre,precio,indicacion,viaAdministracion):
		super().__init__(nombre,precio)
		self.indicacion=indicacion
		self.viaAdministracion=viaAdministracion
	def __str__(self):
		return "Nombre: "+self.nombre+" Precio: "+str(self.precio)
class Farmacia:
	def __init__(self,nombre,ubicacion):
		self.nombre=nombre
		self.ubicacion=ubicacion
		self.medicamentos=[]
		self.cosmeticos=[]
	def agregar(self,producto):
		if isinstance(producto,Medicamento):
			self.medicamentos.append(producto)
		elif isinstance(producto,Cosmetico):
			self.cosmeticos.append(producto)
		else:
			print("no se ha clasificado el preducto")
	def mostrarP(self):
		print("Cosmeticos:")
		for i in range(len(self.cosmeticos)):
			print(self.cosmeticos[i])
			print("Medicamentos:")
		for j in range(len(self.medicamentos)):
			print(self.medicamentos[j])
	def __str__(self):
		
		return "Nombre: "+self.nombre+" Ubicacion: "+self.ubicacion
	
class Registro:
	def __init__(self,fecha,descripcion):
		self.fecha=fecha
		self.descripcion=descripcion
		self.farmacias=[]	
	def agregar(self,farmacia:Farmacia):
		self.farmacias.append(farmacia)
	def mostrar(self):
		for i in range(len(self.farmacias)):
			print(self.farmacias[i])
r1=Registro("19 oct 2025","farmacias de Ceja")
f1=Farmacia("Dolores","Ceja")
f2=Farmacia("Remedios","Ceja")
c1=Cosmetico("Crema nivea",4,"Nivea","Semisolido")
c2=Cosmetico("Labial mate", 25.50, "Maybelline", "sólido")
m1=Medicamento("Paracetamol 500mg", 12.0, "Alivio del dolor y la fiebre", "oral")
m2=Medicamento("Ibuprofeno 400mg", 15.0, "Antiinflamatorio y analgésico", "oral")
f1.agregar(c1)
f2.agregar(c2)
f1.agregar(m1)
f2.agregar(m2)
r1.agregar(f1)
r1.agregar(f2)
print(f1)
f1.mostrarP()
r1.mostrar()

