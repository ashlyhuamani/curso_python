

# Lista de mascotas original con 4 diccionarios
mascotas_original = [
    {"nombre": "Luna", "especie": "Perro", "edad": 3},
    {"nombre": "Max", "especie": "Gato", "edad": 5},
    {"nombre": "Coco", "especie": "Pájaro", "edad": 2},
    {"nombre": "Toby", "especie": "Conejo", "edad": 1}
]

# Mostrar la lista original con los 4 diccionarios
print("Lista original con 4 diccionarios:")
for mascota in mascotas_original:
    print(mascota)
print()

# Crear una copia de la lista original para no modificarla directamente
mascotas_modificadas = mascotas_original.copy()

# Editar el tercer registro (índice 2) cambiándole la edad sin modificar la lista original
mascotas_modificadas[2] = {**mascotas_modificadas[2], "edad": 4}

# Mostrar la lista original y la lista con el tercer registro modificado
print("Lista original:")
for mascota in mascotas_original:
    print(mascota)
print()

print("Lista con el tercer registro modificado (cambiando la edad):")
for mascota in mascotas_modificadas:
    print(mascota)
print()

# Mostrar la lista original y luego la lista con el tercer registro modificado
print("Lista original:")
for mascota in mascotas_original:
    print(mascota)
print()

print("Lista con el tercer registro modificado:")
for mascota in mascotas_modificadas:
    print(mascota)

___________________________

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




# crear una lista de numeros enteros del siguiente texto 
# texto="1,4,8,9,6"
# nueva_lista=[]
# for n texto.split(",")
#    nueva_lista.append(int(n))
# print(nueva lista)
# aplicando la tecnica vlc valor bucle y condicion

# texto="1,4,8,9,6"
# neuva_lista=[int(n)for n in texto.split(",")if n%2==0]
# print(nueva_lista)

# diccionario por comprension 

lista_amigos("abel","anthony","edith","ruth")
diccionario=()
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)

# aplicando el vlc
lista_amigos("abel","anthony","edith","ruth")
diccionario=(amigo:len(amigo)for amigo in lista_amigos)
print(diccionario)

s