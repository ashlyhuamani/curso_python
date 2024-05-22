horarios_disponibles = {
    "9:00": {"disponible": True, "reservado": False, "costo": 20},
    "10:00": {"disponible": True, "reservado": False, "costo": 20},
    "11:00": {"disponible": False, "reservado": False, "costo": 20},
    "12:00": {"disponible": True, "reservado": False, "costo": 20}
}

reserva_realizada = False
fecha_reserva = ""
hora_reserva = ""
costo_reserva = 0

# Caso de uso: Ver lista de horarios disponibles
print("Horarios disponibles:")
for horario, info in horarios_disponibles.items():
    if info["disponible"]:
        print(horario)

# Caso de uso: Reservar en uno de los horarios disponibles
hora_seleccionada = input("Seleccione un horario para reservar: ")
if hora_seleccionada in horarios_disponibles and horarios_disponibles[hora_seleccionada]["disponible"]:
    horarios_disponibles[hora_seleccionada]["reservado"] = True
    fecha_reserva = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
    hora_reserva = hora_seleccionada
    reserva_realizada = True
    print("Reserva realizada para el", fecha_reserva, "a las", hora_reserva)
else:
    print("El horario seleccionado no está disponible.")

# Caso de uso: Pagar por el alquiler de la reserva realizada
if reserva_realizada:
    monto_pago = int(input("Ingrese el monto a pagar por el alquiler: "))
    costo_reserva = monto_pago
    print("Pago realizado por un monto de", monto_pago)
else:
    print("No se ha realizado ninguna reserva.")

# Caso de uso: Verificar detalles del alquiler realizado
if reserva_realizada:
    print("Detalles de la reserva:")
    print("Fecha:", fecha_reserva)
    print("Hora:", hora_reserva)
    print("Costo de alquiler:", costo_reserva)
else:
    print("No se ha realizado ninguna reserva.")