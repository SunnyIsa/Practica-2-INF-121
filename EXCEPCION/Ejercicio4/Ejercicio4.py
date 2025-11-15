#Ejercicio 4. Un sistema de inventario debe controlar errores en la gestión de productos:
class ProductoNoEncontradoException(Exception):
    def __init__(self,m):
        super().__init__(m)
class StockInsuficienteException(Exception):
    def __init__(self,m):
        super().__init__(m)
#a) Crear una clase Producto con atributos (codigo, nombre, precio y stock).
class Producto:
    def __init__(self,codigo,nombre,precio,stock):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
    def __str__(self):
        return "Codigo: {} | Nombre: {} | Precio: {} | Stock: {}".format(self.codigo,self.nombre,self.precio,self.stock)
#b) Crear la clase Inventario que contenga un vector de productos.
class Inventario:
    def __init__(self):
        self.productos=[]
    #c) Implementar un método agregarProducto(Producto p) que lance una excepción si el código ya existe o si el precio/stock son negativos.
    def agregarProducto(self,p):
        if  p in self.productos:
            raise ValueError("el producto ya existe")
        elif p.precio<0:
            raise ValueError("el precio es negativo")
        elif p.stock <0:
            raise ValueError("el stock es negativo")
        else:
            self.productos.append(p)
    #d) Implementar un método buscarProducto(String codigo) que lance una excepción personalizada ProductoNoEncontradoException si no existe.
    def buscarProducto(self,codigo):
        for i in range(len(self.productos)):
            if codigo==self.productos[i].codigo:
                return self.productos[i]
        raise ProductoNoEncontradoException("el producto no se encontro")
#e) Implementar un método venderProducto(String codigo, int cantidad) que reduzca
#el stock si hay suficiente, de lo contrario lance una excepción
#StockInsuficienteException.
    def venderProducto(self,codigo,cantidad):
        if self.buscarProducto(codigo).stock>=cantidad:
            self.buscarProducto(codigo).stock-=cantidad
            print("Se vendio {} quedan {}".format(self.buscarProducto(codigo).nombre,self.buscarProducto(codigo).stock))
        else:
            raise StockInsuficienteException("no hay suficiente stock")
            
            
i1=Inventario()
p1 = Producto("P001", "Laptop Lenovo", 4500.0, 10)
p2 = Producto("P002", "Mouse Logitech", -150.0, 50)
p3 = Producto("P003", "Teclado Mecánico", 320.0, -30)
p4 = Producto("P004", "Monitor Samsung", 1800.0, 15)
p5 = Producto("P005", "Memoria USB 64GB", 80.0, 100)
i1.agregarProducto(p1)

try:
    i1.agregarProducto(p1)
except Exception as e:
    print(e)
try:
    i1.agregarProducto(p2)
except Exception as e:
    print(e)
try:
    i1.agregarProducto(p3)
except Exception as e:
    print(e)
try:
    i1.agregarProducto(p4)
    i1.agregarProducto(p5)
    print(i1.buscarProducto("P004"))
    print(i1.buscarProducto("P003"))
except Exception as e:
    print(e)
try:
    i1.venderProducto("P001",5)
    i1.venderProducto("P001",6)
except Exception as e:
    print(e)
