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


#ejercicio 2
# crear una clase de agencia
# con sus atributos nombre y apellido del pasajero dni numero de asiento fecha de viaje
# sus metodos seran ingresar origen, ingresar destino, cancelar viaje, ver estado de pasaje 


class Agencia:
    def __init__(self, nombre, apellido, dni, numero_asiento, fecha_viaje):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_asiento = numero_asiento
        self.fecha_viaje = fecha_viaje
        self.origen = None
        self.destino = None
        self.estado_pasaje = "Pendiente"

    def ingresar_origen(self, origen):
        self.origen = origen
        self.estado_pasaje = "En proceso"

    def ingresar_destino(self, destino):
        self.destino = destino
        self.estado_pasaje = "Confirmado"

    def cancelar_viaje(self):
        self.estado_pasaje = "Cancelado"
        print(f"El viaje del pasajero {self.nombre} {self.apellido} ha sido cancelado.")

    def ver_estado_pasaje(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Número de asiento: {self.numero_asiento}")
        print(f"Fecha de viaje: {self.fecha_viaje}")
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        print(f"Estado del pasaje: {self.estado_pasaje}")


pasajero1 = Agencia("Juan", "Pérez", "12345678A", 25, "2024-03-15")
pasajero1.ingresar_origen("Madrid")
pasajero1.ingresar_destino("Barcelona")
pasajero1.ver_estado_pasaje()
pasajero1.cancelar_viaje()
pasajero1.ver_estado_pasaje()
