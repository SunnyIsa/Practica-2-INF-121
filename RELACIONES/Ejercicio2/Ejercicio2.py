class Departamento:
    def __init__(self,nombre,area):
        self.__nombre=nombre
        self.__area=area
        self.__empleado=[]
        self.__nroEmp=0
    def emplea(self,e):
        self.__empleado.append(e)
        self.__nroEmp+=1
    def getNombre(self):
        return self.__nombre
    def getEmpleados(self):
        return self.__empleado
    #b) Agregar el metodo mostrarEmpleados()
    def mostrarEmpleados(self) :
        print(self.__nombre)
        if self.__empleado != []:
            for i in range(self.__nroEmp):
                print(self.__empleado[i])
        else:
            print("no hay empleados ")
    #c) Implementar cambioSalario() para todos los empleados de un departamento en específico.
    def cambioSalario(self,x):
        for i in range(self.__nroEmp):
            self.__empleado[i].setSueldo(x)
    #d) Verificar si algun empleado del departamento 1 pertenece al departamento 2.
    def verificar(self,d):
        b=d.getEmpleados()
        r=len(b)
        for i in range(self.__nroEmp):
            for j in range(r):
                if self.__empleado[i].getNombre()==b[j].getNombre():
                    print("El empleado {} esta en ambos departamentos {} y {}".format(self.__empleado[i].getNombre(),self.__nombre,d.getNombre()))
    def mover(self,d):
        for i in range(self.__nroEmp):
            if self.__empleado[i] not in d.getEmpleados():
                d.emplea(self.__empleado[i])
        self.__empleado=[]
        self.__n=0
        
			
#Ejercicio 2. Defina las clases:
class Empleado:
    def __init__(self,nombre,cargo,sueldo):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__sueldo=sueldo
    def getNombre(self):
        return self.__nombre
    def setSueldo(self,x):
        self.__sueldo=self.__sueldo+(self.__sueldo*x/100)
    def __str__(self):
        return "Empleado:[Nombre: {} | Cargo: {} | Sueldo {}]".format(self.__nombre,self.__cargo,self.__sueldo)
		
#a) Instanciar 2 departamentos, uno con 5 empleados y el otro sin empleados.		
e1 = Empleado("Ana", "Contadora", 3500)
e2 = Empleado("Luis", "Analista", 4000)
e3 = Empleado("María", "Diseñadora", 3700)
e4 = Empleado("Pedro", "Técnico", 3200)
e5 = Empleado("Sofía", "Gerente", 5500)

d1 = Departamento("Finanzas", "Administración")
d2 = Departamento("Marketing", "Comercial")

d1.emplea(e1)
d1.emplea(e2)
d1.emplea(e3)
d1.emplea(e4)
d1.emplea(e5)
d1.mostrarEmpleados(
)
d1.cambioSalario(10)
d1.mostrarEmpleados(
)
d2.emplea(e2)
d1.verificar(d2)
#los saldos cambian en porcentajesq
d2.mostrarEmpleados()
#e) Mover los empleados del departamento 1 al departamento 2. Tras eso mostrar de nuevo los departamentos.
d1.mover(d2)
d1.mostrarEmpleados()
d2.mostrarEmpleados()
