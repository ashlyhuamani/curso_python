## crear una funcion que reciba por argumento n numeros y retorna una lista con los numeros pares 

#def numeros_pares(n):
#    return [num for num in range(1, n + 1) if num % 2 == 0]

# Ejemplo de uso de la función
# n = 10
# resultado = numeros_pares(n)
# print(resultado)

## crear tres funciones para los siguiente casos
# calcular el numero menor 
# calcular el numero mayor
# calcular la suma de todos los numeros 
# se la pasara por argumneto n numeros 


# Función para calcular el número menor
#def numero_menor(*args):
#    menor=arsg[0]
#    for n in args:
#        if n<menor:
#            menor=n
#   return menor
# Función para calcular el número mayor
#def numero_mayor(*args):
#    mayor=arsg[0]
#    for n in arsg:
#        if>mayor:
#            mayor=n
#    return mayor

# Función para calcular la suma de todos los números
#def suma_numeros(*args):
#    suma=arsg[0]
#    for n in arsg:
#        if+suma:
#            suma +=n
#    return suma

# Ejemplo de uso de las funciones
#numeros = [10, 5, 20, 8, 15]
#print(numero_menor(*numeros))
#print(numero_mayor(*numeros))
#print(suma_numeros(*numeros))

# tarea
# crear una lista de alumnos con los siguientes campos 
#nombre,apellido, edad celular, email
#1.- actualizar los registros con un campo mas todos tendran en el campo de programas de estudio de enfermeria .
#2. buscar el segundo regitro y actualizar su edad a 50 años  
# Crear la lista de alumnos con los campos solicitados
lista_alumnos = [
    {
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 30,
        "celular": "555-1234",
        "email": "juan.perez@example.com",
        "programas_estudio": "Enfermería"
    },
    {
        "nombre": "Maria",
        "apellido": "Gomez",
        "edad": 40,
        "celular": "555-5678",
        "email": "maria.gomez@example.com",
        "programas_estudio": "Enfermería"
    },
    {
        "nombre": "Pedro",
        "apellido": "Lopez",
        "edad": 35,
        "celular": "555-9012",
        "email": "pedro.lopez@example.com",
        "programas_estudio": "Enfermería"
    }
]

# Actualizar todos los registros con un campo extra de programas de estudio de enfermería
for alumno in lista_alumnos:
    alumno["programas_estudio"] = "Enfermería"

# Buscar el segundo registro y actualizar su edad a 50 años
if len(lista_alumnos) >= 2:
    lista_alumnos[1]["edad"] = 50

# Imprimir la lista de alumnos actualizada
print("Lista de alumnos actualizada:")
for alumno in lista_alumnos:
    print(alumno)