# return devuelve valores que podre hacer uso 
# crear un funcion retorne el numero 10 ,y muestra por terminal si es par 
# siempre que el valor que retorno mi funcion se utilize en mas sentecias 
# u operaciones hacer uso de return
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es impar")
# print solo muestra por terminal 
# return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato 
# un tipo de datos estructurados

# crear una funcion que me muestre el producto de dos numeros 
def producto(a,b):
    return a*b

# crear una funcion que me retorne una lista de tres numeros 
def lista_nuemero():
    return [3,2,6]

# print usaremos cada vez que muestre funcion retorne un mensaje 
# crear una funcion que me por parametro reciba un nombre y retorne un mensaje de
# bienvenida con el nombre

def mensaje(nombre):
    print(f"hola, (nombre), bienvenido al chongo")
mensaje("jose")

# crear un funcion que reciba por parametro una lista de numeros 
# y se devuelve el numero menor , mostrar pro terminal el valor retornando por la funcion 
lista=[4,3,6,78,7]
def Min(l):
    minimo=l[0]
    for n in l:
        if n <minimo:
            minimo=n
    return minimo
print(Min(lista))

# crear una funcion que reciba como parametro el nombre y la edad de una personas al funcion 
# debera retornar un diccionario con los datos , luego mostrar por terminal el valor de retorno 
# en mi funcion

nombre=abel
edad=19
def persona (nom,edad):
    # return {
    "nombre" :nom.
    "edad" :edad
 #  }
 return dict(
     nombre=nom,
     edad=edad
 )
print(persona(nombre.edad))





