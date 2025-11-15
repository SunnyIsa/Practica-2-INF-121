#Ejercicio10. Usando el siguiente diagrama de clases se le pide resolver:
class Persona:
    def __init__(self,nombre,apellido,edad,ci):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.ci=ci
class Participante(Persona):
    def __init__(self,nombre,apellido,edad,ci,nroTicket):
        super().__init__(nombre,apellido,edad,ci)
        self.nroTicket=nroTicket
    def __str__(self):
        return "Nombre: {}, Apellido: {}, Edad: {}, CI: {}, Numero de ticket: {}".format(self.nombre,self.apellido,self.edad,self.ci,self.nroTicket)
class Speaker(Persona):
    def __init__(self,nombre="",apellido="",edad="",ci="",especialidad=""):
        super().__init__(nombre,apellido,edad,ci)
        self.especialidad=especialidad
    def __str__(self):
        return "Nombre: {}, Apellido: {}, Edad: {}, CI: {}, Especialidad: {}".format(self.nombre,self.apellido,self.edad,self.ci,self.especialidad)
class Charla:
    def __init__(self,lugar,nombreCharla):
        self.lugar=lugar
        self.nombreCharla=nombreCharla
        self.S=Speaker()
        self.np=0
        self.P=[None]*50
    def designarSpeak(self,nombre,apellido,edad,ci,especialidad):
        self.S=Speaker(nombre,apellido,edad,ci,especialidad)
    def agregar(self,p):
        for i in range(50):
            if self.P[i]==None:
                self.P[i]=p
                self.np+=1
                break
    def verificar(self,X,Y):
        for i in range(self.np):
            if self.P[i].nombre==X and self.P[i].apellido==Y:
                return True
    def __str__(self):
        return "Lugar: {} | Nombre de charla: {} | Speaker: [{}]| Numero de participantes: {}".format(self.lugar,self.nombreCharla,self.S.__str__(),self.np)
class Evento:
    def __init__(self,nombre):
        self.nombre=nombre
        self.nc=0
        self.C=[None]*50
    def agregar(self,c):
        for i in range(50):
            if self.C[i]==None:
                self.C[i]=c
                self.nc+=1
                break
    #a) Cuál es la edad promedio de los participantes en el evento.
    def promedio(self):
        s=0
        p=0
        for i in range(self.nc):
            for j in range(self.C[i].np):
                s+=self.C[i].P[j].edad
            p+=self.C[i].np
        return "Promedio: "+str(int(s/p))
    #b) Verificar si la persona nombre “X” y apellido “Y” se encuentra en alguna de las charlas tantocomo participante o como Speaker.
    def verificar(self,X,Y):
        b=False
        for i in range(self.nc):
            if self.C[i].verificar(X,Y):
                print("{}{} esta en la charla {} como participante".format(X,Y,self.C[i].nombreCharla))
                b=False
            elif self.C[i].S.nombre==X and self.C[i].S.apellido==Y:
                b=False
                print("{}{} esta en la charla {} como Speaker".format(X,Y,self.C[i].nombreCharla))
        if b:
            print("{}{} no esta en ninguna charla".format(X,Y))
    #c) El speaker con el C.I. X no pudo asistir por lo cual se deberá eliminar todas las charlas que iba a dar.
    def eliminar(self,X):
        c=[]
        for i in range (self.nc):
            if self.C[i].S.ci==X:
                self.C[i]==None
                self.nc-=1
                print("La charla {} se elimino".format(self.C[i].nombreCharla))
            else:
                c.append(self.C[i])
        for j in range(self.nc):
            self.C[j]=c[j]
    #d) Ordenar las charlas por el número de participantes.
    def ordenar(self):
        for i in range(self.nc):
            for j in range(self.nc-i-1):
                if self.C[j].np>self.C[j+1].np:
                    temp=self.C[j]
                    self.C[j]=self.C[j+1]
                    self.C[j+1]=temp
    def __str__(self):
        s=""
        for i in range(self.nc):
            s+=self.C[i]. __str__()+"\n"
        return "Nombre : {} \n{} ".format(self.nombre,s)
p1  = Participante("Ana", "García", 25, 1000001, 1)
p2  = Participante("Luis", "Pérez", 30, 1000002, 2)
p3  = Participante("María", "López", 22, 1000003, 3)
p4  = Participante("Carlos", "Fernández", 28, 1000004, 4)
p5  = Participante("Lucía", "Mendoza", 24, 1000005, 5)
p6  = Participante("Jorge", "Rojas", 31, 1000006, 6)
p7  = Participante("Elena", "Ramírez", 27, 1000007, 7)
p8  = Participante("Pablo", "Cruz", 26, 1000008, 8)
p9  = Participante("Rosa", "Suárez", 29, 1000009, 9)
p10 = Participante("Miguel", "Torres", 33, 1000010, 10)
p11 = Participante("Valeria", "Soto", 21, 1000011, 11)
p12 = Participante("Andrés", "Flores", 35, 1000012, 12)
p13 = Participante("Natalia", "Ruiz", 23, 1000013, 13)
p14 = Participante("Raúl", "Morales", 32, 1000014, 14)
p15 = Participante("Diana", "Aguilar", 25, 1000015, 15)
p16 = Participante("Fernando", "Linares", 26, 1000016, 16)
p17 = Participante("Gabriela", "Salazar", 24, 1000017, 17)
p18 = Participante("Hugo", "Delgado", 28, 1000018, 18)
p19 = Participante("Isabel", "Paz", 27, 1000019, 19)
p20 = Participante("Julio", "Campos", 29, 1000020, 20)
p21 = Participante("Karen", "Montes", 30, 1000021, 21)
p22 = Participante("Leonardo", "Villalba", 22, 1000022, 22)
p23 = Participante("Marta", "Quispe", 23, 1000023, 23)
p24 = Participante("Nicolás", "Vargas", 31, 1000024, 24)
p25 = Participante("Olga", "Silva", 28, 1000025, 25)
p26 = Participante("Pedro", "Gómez", 26, 1000026, 26)
p27 = Participante("Raquel", "López", 27, 1000027, 27)
p28 = Participante("Samuel", "Mamani", 25, 1000028, 28)
p29 = Participante("Teresa", "Huanca", 32, 1000029, 29)
p30 = Participante("Ulises", "Choque", 33, 1000030, 30)

c1 = Charla("Auditorio Central", "Transformación Digital en la Educación")
c2 = Charla("Sala A", "El futuro de la IA en Latinoamérica")
c3 = Charla("Sala B", "Ciberseguridad para todos")

c1.designarSpeak("Ricardo", "Navarro", 45, 2000001, "Inteligencia Artificial")
c2.designarSpeak("Beatriz", "López", 38, 2000002, "Educación Digital")
c3.designarSpeak("Hernán", "Serrano", 50, 2000003, "Ciberseguridad")

e1= Evento("Congreso Internacional de Tecnología 2025")
c1.agregar(p1)
c1.agregar(p2)
c1.agregar(p3)
c1.agregar(p4)
c1.agregar(p5)
c1.agregar(p6)
c1.agregar(p7)
c1.agregar(p8)
c1.agregar(p9)
c1.agregar(p10)
c2.agregar(p11)
c2.agregar(p12)
c2.agregar(p13)
c2.agregar(p14)
c2.agregar(p15)
c2.agregar(p16)
c2.agregar(p17)
c2.agregar(p18)
c3.agregar(p19)
c3.agregar(p20)
c3.agregar(p21)
c3.agregar(p22)
c3.agregar(p23)
c3.agregar(p24)
c3.agregar(p25)
c3.agregar(p26)
c3.agregar(p27)
c3.agregar(p28)
c3.agregar(p29)
c3.agregar(p30)
e1.agregar(c1)
e1.agregar(c2)
e1.agregar(c3)
print(e1)
print(e1.promedio())
e1.verificar("Natalia", "Ruiz")
e1.verificar("Beatriz", "López")
e1.eliminar(2000002)
print()
print(e1)

c1.agregar(p10)
c1.agregar(p11)
c1.agregar(p12)
e1.ordenar()
print()
print(e1)














            


                
                
        
            
        
        
        
            
        
        
