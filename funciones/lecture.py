# return devuelve valores que podre hacer uso 
# crear un funcion retorne el numero 10 ,y muestra por terminal si es par 
# siempre que el valor que retorno mi funcion se utilize en mas sentecias 
# u operaciones hacer uso de return
# def diez():
#   return 10
# if diez()%2==0:
#   print("es par")
# else:
#    print("es impar")
# print solo muestra por terminal 
# return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato 
# un tipo de datos estructurados

# crear una funcion que me muestre el producto de dos numeros 
#def producto(a,b):
#   return a*b

# crear una funcion que me retorne una lista de tres numeros 
# def lista_nuemero():
#    return [3,2,6]

# print usaremos cada vez que muestre funcion retorne un mensaje 
# crear una funcion que me por parametro reciba un nombre y retorne un mensaje de
# bienvenida con el nombre

# def mensaje(nombre):
#    print(f"hola, (nombre), bienvenido al chongo")
# mensaje("jose")

# crear un funcion que reciba por parametro una lista de numeros 
# y se devuelve el numero menor , mostrar pro terminal el valor retornando por la funcion 
#lista=[4,3,6,78,7]
#def Min(l):
#   minimo=l[0]
#    for n in l:
#        if n <minimo:
#            minimo=n
#    return minimo
# print(Min(lista))

# crear una funcion que reciba como parametro el nombre y la edad de una personas al funcion 
# debera retornar un diccionario con los datos , luego mostrar por terminal el valor de retorno 
# en mi funcion

# nombre=abel
# edad=19
# def persona (nom,edad):
# return {
#    "nombre" :nom.
#   "edad" :edad
#  }
# return dict(
#     nombre=nom,
#     edad=edad
#   )
# print(persona(nombre.edad))


# def suma (*arsg):
#   nueva_lista=list(arsg)
#   nueva_lista=[0]=10
#    print(nueva-.lista)
# suma(4,7,8,5,2,4)

# empaquetar y desampaquetar de argumento nominales 
#def alumnos (**kwargs):
#    kwargs["nombre"]="abel"
#    print(kwargs)
#alumnos(nombre="miguel",apellido"largo",edad=30)

## ejemplo de lambda
#saludo=lambda n:f "hola, {n] , {a}"
#print(saludo("ruth","castillo"))

# crear un programa anonimo que reciba como parametro una lista de 5 numeros y retorne dos listas una con
# los numeros pares y otra con numeros impares

# Definir la lista de 5 números de ejemplo
numeros = [23, 4, 11, 8, 17]

# Crear funciones lambda para separar los números pares e impares
separar_pares_impares = lambda numeros: ([x for x in numeros if x % 2 == 0], [x for x in numeros if x % 2 != 0])

# Obtener las listas de números pares e impares sin filtrar
numeros_pares, numeros_impares = separar_pares_impares(numeros)

# Imprimir los resultados
print("Números pares:", numeros_pares)
print("Números impares:", numeros_impares)

int(input())

def mensaje(m:funciones)
    print(m)
def pedir_nombre()
    nombre=input("ingresar nombre")
    return nombre
mensaje(pedir_nombre())