#Ejercicio 6. Sea la clase CuentaBancaria con los siguientes atributos: numeroCuenta (String), titular (String), saldo (double)
#a) Cree la excepción personalizada FondosInsuficientesException, que se lance cuando se intente retirar un monto mayor al saldo disponible.
class FondosInsuficientesException(Exception):
    def __init__(self,m):
        super().__init__(m)
class CuentaBancaria:
    def __init__(self,numeroCuenta,titular,saldo):
        self.numeroCuenta=numeroCuenta
        self.titular=titular
        self.saldo=saldo
    #b) Implemente los métodos:
#• depositar(double monto) → aumenta el saldo si el monto es positivo, si no,
#lanza una excepción IllegalArgumentException.
#• retirar(double monto) → descuenta el saldo si hay fondos suficientes, de lo
#contrario lanza FondosInsuficientesException.
#• mostrarInfo() → imprime en pantalla número de cuenta, titular y saldo.
    def depositar(self,monto):
        if monto<0:
            raise ValueError("el monto no es valido")
        else:
            self.saldo+=monto
            print("se deposito el monto ,tu saldo es: {}".format(self.saldo))
    def retirar(self,monto):
        if monto>self.saldo:
            raise FondosInsuficientesException("No tienes suficiente saldo")
        else:
            self.saldo-=monto
            print("se retiro el monto ,tu saldo es: {}".format(self.saldo))
    def mostrarInfo(self):
        print("Numero de cuenta: {} | Titular: {} | Saldo: {}".format(self.numeroCuenta,self.titular,self.saldo))
#c) Cree un programa principal que:
#• Genere una cuenta con número "12345", titular "Juan Pérez", y saldo inicial de 1000.
#• Realice un depósito válido y otro con monto negativo para disparar la excepción.
#• Realice un retiro válido y otro que supere el saldo para disparar la excepción personalizada.
#• Use bloques try-catch para capturar y mostrar los errores.
c1= CuentaBancaria("12345", "Juan Pérez", 1000)
try:
    c1.depositar(10)
    c1.depositar(-1)
except Exception as e:
    print(e)
try:
    c1.retirar(10)
    c1.retirar(1001)
except Exception as e:
    print(e)
    
