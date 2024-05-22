# Lista de horarios disponibles
horarios_disponibles = [
    {"fecha": "2022-06-01", "hora_inicio": "10:00", "hora_fin": "12:00"},
    {"fecha": "2022-06-02", "hora_inicio": "14:00", "hora_fin": "16:00"},
    {"fecha": "2022-06-03", "hora_inicio": "09:00", "hora_fin": "11:00"},
    # Agrega más horarios disponibles según sea necesario
]

# Variable para almacenar la reserva del usuario
reserva = {}

# Función para mostrar la lista de horarios disponibles
def mostrar_horarios_disponibles():
    print("Horarios disponibles:")
    for i, horario in enumerate(horarios_disponibles, start=1):
        print(f"{i}. Fecha: {horario['fecha']}, Hora de inicio: {horario['hora_inicio']}, Hora de fin: {horario['hora_fin']}")

# Función para reservar un horario
def reservar_horario():
    mostrar_horarios_disponibles()
    opcion = int(input("Selecciona el número de horario que deseas reservar: "))
    if opcion >= 1 and opcion <= len(horarios_disponibles):
        horario_seleccionado = horarios_disponibles[opcion - 1]
        reserva["fecha"] = horario_seleccionado["fecha"]
        reserva["hora_inicio"] = horario_seleccionado["hora_inicio"]
        reserva["hora_fin"] = horario_seleccionado["hora_fin"]
        print("Has realizado la reserva exitosamente.")
    else:
        print("Opción inválida.")

# Función para realizar el pago
def realizar_pago():
    # Lógica para realizar el pago, puedes integrar con una pasarela de pago o utilizar métodos de prueba
    monto = float(input("Ingresa el monto a pagar: "))
    reserva["monto"] = monto
    print(f"Se ha realizado el pago exitosamente por un monto de {monto}.")

# Función para verificar el alquiler y mostrar los detalles
def verificar_alquiler():
    if reserva:
        print("Detalles de la reserva:")
        print(f"Fecha: {reserva['fecha']}")
        print(f"Hora de inicio: {reserva['hora_inicio']}")
        print(f"Hora de fin: {reserva['hora_fin']}")
        print(f"Monto pagado: {reserva['monto']}")
    else:
        print("No tienes ninguna reserva realizada.")

# Flujo principal del programa
mostrar_horarios_disponibles()
reservar_horario()
realizar_pago()
verificar_alquiler()