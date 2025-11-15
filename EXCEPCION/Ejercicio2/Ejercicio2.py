#Ejercicio 2. Se desea crear una calculadora que realice operaciones básicas, manejando errores comunes:
class NumeroInvalidoException(Exception):
    def __init__(self,m):
        super().__init__(m)
#a) Crear la clase Calculadora con métodos estáticos para sumar, restar, multiplicar y dividir.
class Calculadora:
    @staticmethod
    def sumar(x,y):
        return x+y
    @staticmethod
    def restar(x,y):
        return x-y
    @staticmethod
    def multiplicar(x,y):
        return x*y
    @staticmethod
    #b) El método dividir debe lanzar una excepción ArithmeticException si el divisor es cero.
    def dividir(x,y):
        if y==0:
            raise ArithmeticError("No se puede dividir entre cero")
        else:
            return x/y
    #c) Implementar un método que convierta un String a número entero, lanzando una excepción personalizada NumeroInvalidoException si el valor no es numérico.
    @staticmethod
    def convertir(x):
        try:
            return int(x)
        except ValueError as e:
            raise NumeroInvalidoException("Solo ingrese numeros")
#d) Crear un programa principal que pruebe todos los métodos, incluyendo casos con error.
print(Calculadora.sumar(5, 3))
print(Calculadora.restar(10, 4))
print(Calculadora.multiplicar(2, 6))
try:
    print(Calculadora.dividir(10, 2))
except ArithmeticError as e:
    print(e)
try:
    print(Calculadora.dividir(10, 0))
except ArithmeticError as e:
    print(e)
try:
    print(Calculadora.convertir("123"))
except NumeroInvalidoException as e:
    print(e)
try:
    print(Calculadora.convertir("hola"))
except NumeroInvalidoException as e:
    print(e)
