#Ejercicio 12. Crea una relación de agregación entre Hospital y Doctor. Los doctores pueden trabajar en distintos hospitales.
#a) Crea la clase Doctor con atributos nombre, especialidad.
class Doctor:
    def __init__(self,nombre,especialidad):
        self.nombre=nombre
        self.especialidad=especialidad
    def __str__(self):
        return "Nombre: {} , Especialidad: {}".format(self.nombre,self.especialidad)
#b) Crea la clase Hospital que tiene una lista de doctores.
class Hospital:
    def __init__(self,nombre):
        self.nombre=nombre
        self.doctores=[]
    def asignar(self,d):
        self.doctores.append(d)
    def __str__(self):
        s=""
        for i in range(len(self.doctores)):
            s+=self.doctores[i].__str__()+"\n"
        return "Nombre: {} \nDoctores:\n{}".format(self.nombre,s)
#c) Permite asignar doctores a hospitales y mostrar los doctores de cada hospital
h1 = Hospital("Hospital Central")
h2 = Hospital("Clínica La Paz")
h3 = Hospital("Hospital del Sur")

d1 = Doctor("Carlos Pérez", "Cardiología")
d2 = Doctor("Elena Rojas", "Pediatría")
d3 = Doctor("Miguel Flores", "Neurología")
d4 = Doctor("Lucía Gutiérrez", "Traumatología")
d5 = Doctor("Andrés Morales", "Dermatología")
d6 = Doctor("Sofía Aguilar", "Oncología")
h1.asignar(d1)
h1.asignar(d2)
h1.asignar(d3)
h1.asignar(d4)
h2.asignar(d1)
h2.asignar(d5)
h3.asignar(d2)
h3.asignar(d6)
print(h1)
print(h2)
print(h3)
