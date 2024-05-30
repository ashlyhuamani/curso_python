

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