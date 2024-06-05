# mostrar lista con los 4 diccionarios 
#editar el 3ro registro y cambiarle la edad sin modificar la lista original 
# mostrar la lista original y luego la lista con el registo y cambiarle la edad sin modificar la lista original
#mostrar la lista original y luego la lista con el 3ro registro modificado.

# Lista de registros original con 4 diccionarios
registros_original = [
    {"id": 1, "nombre": "Alice", "edad": 25},
    {"id": 2, "nombre": "Bob", "edad": 30},
    {"id": 3, "nombre": "Charlie", "edad": 35},
    {"id": 4, "nombre": "David", "edad": 40}
]

# Paso 1: Mostrar la lista original con los 4 diccionarios
print("Lista original con 4 diccionarios:")
for registro in registros_original:
    print(registro)
print()

# Paso 2: Crear una copia del tercer registro para no modificar la lista original directamente
tercer_registro_copia = registros_original[2].copy()

# Paso 3: Editar la copia del tercer registro cambiando la edad
tercer_registro_copia["edad"] = 38

# Paso 4: Mostrar la lista original y la lista con el tercer registro modificado
print("Lista original:")
for registro in registros_original:
    print(registro)
print()

print("Lista con el tercer registro modificado (cambiando la edad):")
registros_modificados = registros_original.copy()
registros_modificados[2] = tercer_registro_copia
for registro in registros_modificados:
    print(registro)

 # yo como dueño de si mascota 
# deseo ver una lista de mis mascotas 
# para tomar un resumen o control de ellos   

# Lista de mascotas con diccionarios para cada mascota
mascotas = [
    {"nombre": "Luna", "especie": "Perro", "edad": 3},
    {"nombre": "Max", "especie": "Gato", "edad": 5},
    {"nombre": "Coco", "especie": "Pájaro", "edad": 2},
    # Agrega más mascotas según sea necesario
]

# Función para mostrar la lista de mascotas
def mostrar_mascotas():
    print("Lista de mascotas:")
    for mascota in mascotas:
        print(f"Nombre: {mascota['nombre']}, Especie: {mascota['especie']}, Edad: {mascota['edad']} años")
    print()

# Mostrar la lista de mascotas
mostrar_mascotas()

# un empresario de alquiler de autos desea guardar en una base de datos la informacion de sus vehiculos,
# proceso que desea automatizar con un sitema informatico, las acciones que puede realizar el empresario 
# son ver las listas de autos que tiene, podra tambien actualizar la lista y agregar un nuevo vehiculo 

####
# casos de usos 
# tipos de vehiculos 
# listas de vehiculos disponibles
# precio 
# programación 

# Base de datos de vehículos de alquiler
vehiculos = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "año": 2020, "precio": 50, "disponible": True},
    {"id": 2, "marca": "Honda", "modelo": "Civic", "año": 2019, "precio": 45, "disponible": False},
    # Agrega más vehículos según sea necesario
]

# Función para mostrar la lista de autos disponibles
def mostrar_autos():
    print("Lista de autos disponibles:")
    for vehiculo in vehiculos:
        print(f"ID: {vehiculo['id']}, Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Año: {vehiculo['año']}, Precio: ${vehiculo['precio']}, Disponible: {vehiculo['disponible']}")
    print()

# Función para actualizar la información de un vehículo existente
def actualizar_vehiculo(id_vehiculo, campo, nuevo_valor):
    for vehiculo in vehiculos:
        if vehiculo["id"] == id_vehiculo:
            vehiculo[campo] = nuevo_valor
            print(f"Se ha actualizado el campo '{campo}' del vehículo con ID {id_vehiculo}.")
            return
    print(f"No se encontró un vehículo con ID {id_vehiculo}.")

# Función para agregar un nuevo vehículo
def agregar_vehiculo(marca, modelo, año, precio, disponible):
    id_nuevo = len(vehiculos) + 1
    vehiculo_nuevo = {"id": id_nuevo, "marca": marca, "modelo": modelo, "año": año, "precio": precio, "disponible": disponible}
    vehiculos.append(vehiculo_nuevo)
    print("Se ha agregado un nuevo vehículo a la base de datos.")
    
# Ejemplo de uso de las funciones
mostrar_autos()
actualizar_vehiculo(1, "precio", 55)
agregar_vehiculo("Ford", "Focus", 2018, 40, True)
mostrar_autos()


# crear una lista de los primeros 20 numeros primos haciendo uso de conprecion

# Crear una lista de los primeros 20 números primos utilizando comprensión de listas sin definir una función
numeros_primos = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1) if num != i)]

# Tomar los primeros 20 números primos de la lista generada
primeros_20_primos = [num for num in numeros_primos][:20]

print(primeros_20_primos)










