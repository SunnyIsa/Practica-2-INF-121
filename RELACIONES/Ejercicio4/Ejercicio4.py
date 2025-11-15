#Ejercicio 4. Sea la clase ropero (material, Ropa[20], nroRopas) y la clase Ropa(tipo, material)
#a) Realizar el diagrama de clases
class Ropero:
    def __init__(self,material):
        self.material=material
        self.nroRopas=0
        self.Ropa=[None]*20
    #b) Adicionar N prendas al ropero
    def agregar(self,r):
        n=0
        for i in range(self.nroRopas,20):
            if self.Ropa[i]==None and n<len(r):
                self.Ropa[i]=r[n]
                n+=1
                self.nroRopas+=1
            else:
                break
    #c) Eliminar las prendas de material x o de tipo y d) mostrar las prendas de materia X y de tipo.
    def eliminar(self,x):
        r=[]
        for i in range(self.nroRopas):
            if x!=self.Ropa[i].material and x!=self.Ropa[i].tipo:
                r.append(self.Ropa[i])
        self.nroRopas=len(r)
        for j in range(self.nroRopas):
            self.Ropa[j]=r[j]
        for k in range(self.nroRopas,20):
            self.Ropa[k]=None
        return self
    def mostrar(self,x,y):
        for i  in range(self.nroRopas):
            if x==self.Ropa[i].tipo and y==self.Ropa[i].material:
                print(self.Ropa[i])
class Ropa:
    def __init__(self,tipo,material):
        self.tipo=tipo
        self.material=material
    def __str__(self):
        return "Tipo: {} | Material : {}".format(self.tipo,self.material)
r1=Ropero("Madera")
p1=Ropa("Pantalon","Jean")
p2=Ropa("Polera","Algodon")
p3=Ropa("Chompa","Lana")
p4=Ropa("Polera","Algodon")
p5=Ropa("Calcetines","Lana")
r1.agregar([p1,p2,p3,p4,p5])
r1.eliminar("Lana")
print(r1.Ropa[0])
print(r1.Ropa[1])
print(r1.Ropa[2])
print(r1.Ropa[3])
print(r1.Ropa[4])
r1.mostrar("Polera","Algodon")

    
        
