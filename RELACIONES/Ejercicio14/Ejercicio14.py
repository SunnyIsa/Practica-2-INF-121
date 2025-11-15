#Ejercicio 14. Agregación: Empresa y empleados
#• Clase Empleado con los atributos: nombre, puesto, salario
#• Clase Empresa con los atributos: nombre, empleados (vector de objetos Empleado) Se pide:
class Empleado:
    def __init__(self,nombre,puesto,salario):
        self.nombre=nombre
        self.puesto=puesto
        self.salario=salario
    def __str__(self):
        return "Nombre: {} | Puesto: {} | Salario: {} ".format(self.nombre,self.puesto,self.salario)
class Empresa:
    def __init__(self,nombre):
        self.nombre=nombre
        self.empleados=[]
    def agregar(self,e):
        if e not in self.empleados:
            self.empleados.append(e)
    #c) Implementar un método en Empresa para buscar un empleado por nombre y retornar su información.       
    def buscar(self,x):
        for i in range(len(self.empleados)):
            if x==self.empleados[i].nombre:
                return self.empleados[i].__str__()
        return "Este empleado no esta en esta  empresa "
    #d) Crear un método para eliminar un empleado de la empresa por nombre.
    def eliminar(self,x):
        for i in range(len(self.empleados)):
            if x==self.empleados[i].nombre:
                print("Se elimino el empleado {}".format(self.empleados[i].__str__()))
                self.empleados.remove(self.empleados[i])
                break
        return self
    #e) Agregar un método que calcule y muestre el promedio salarial de todos los empleados.
    def promedio(self):
        s=0
        for i in range(len(self.empleados)):
            s+=self.empleados[i].salario
        return "Promedio "+str(s/len(self.empleados))
    #Implementar un método para listar todos los empleados que tengan un salario mayor a un valor dado.
    def salMayor(self,x):
        for i in range(len(self.empleados)):
            if x<self.empleados[i].salario:
                print(self.empleados[i])
        return self
    def __str__(self):
        s=""
        for i in range(len(self.empleados)):
            s+=self.empleados[i].__str__()+"\n"
        return "Nombre: {} \nEmpleados \n{}".format(self.nombre,s)
#a) Crear una empresa y agregar varios empleados
em1= Empresa("TechSolutions")

e1 = Empleado("Ana López", "Desarrolladora", 4500.50)
e2 = Empleado("Carlos Pérez", "Diseñador", 3800.75)
e3 = Empleado("María Gómez", "Gerente", 6200.00)
e4 = Empleado("Luis Torres", "Analista", 4100.25)
e5 = Empleado("Sofía Ramírez", "Soporte Técnico", 3500.00)

em1.agregar(e1)
em1.agregar(e2)
em1.agregar(e3)
em1.agregar(e4)
em1.agregar(e5)

print(em1.buscar("María Gómez"))
print()
#b) Mostrar la información de la empresa y sus empleados.
print(em1)
print(em1.eliminar("María Gómez"))
print(em1)
print(em1.promedio())
print(em1.salMayor(3500))
        
        
        
