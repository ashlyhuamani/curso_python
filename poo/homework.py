# crear una clase banco 
# sus atributos seran nombre,aplellido,dni, numero de cuenta y saldo inicial
#como metodos podremos hacer deposito retirar dinero ver estado de cuenta

class Banco:
    def __init__(self, nombre, apellido, dni, numero_cuenta, saldo_inicial):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado correctamente. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad de depósito debe ser mayor que cero.")

    def retiro(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado correctamente. Nuevo saldo: {self.saldo}")
        elif cantidad > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("La cantidad de retiro debe ser mayor que cero.")

    def ver_estado_cuenta(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Saldo actual: {self.saldo}")


