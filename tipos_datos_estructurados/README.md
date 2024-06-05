# tipos de datos estructurados (TDA- tipos de datos abstractos)

# lista - sus valores o elemtos se pueden actualizar, eliminar.

<!-- python 

lista=["abel",20,5.2,.5,False,["texto",.2]]
#tupla - sus valores o elementos no pueden ser modificados o eliminados.
tupla=("abel",20,5.2,,False,[])

#diccionarios o objetos 
#loa diccionarios almacenan los datos con clave :valor
diccionario={"nombre":"antonio", "edad":15 "sexo":False}

- {!TIP}
- *OBSERVACION* Que los tipos de datos estruccturados pueden almacenar en su interior otros tipos de datos estructurados.

python
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":20,
        "amigos":["no tiene"]
    },{
        "nombre":"ruth",
        "edad":13
        "amigos":["flor", "rosio"]
    },{
        "nombre":"rony",
        "edad":23
        "amigos"["no tiene"]
    }

]

## metodos 
### 1. convertir texto a lista 
python
texto="hola"
list(texto)
#["h","o","l","a"]

# METODO SPLIT - trocea textos mediante un limitador ejemplo 
texto="hola como estan mascotas"
texto.split(",")


# join es el metodo que utilizamos para unir elemtos de una sola lista 

texto_largo="este es un texto largo chiquitas y chiquitos"
nuevo_texto=texto_largo.split(" ")
print(" ".join(nuevo_texto))


### 2. agregar elementos a una lista 
python
#metodo append - es el metodo que me permite agregar elementos al final de una lista 
lista=["hola"]
lista.append("mundo")
print(lista)
#["hola","mundo"]

# metodo insert - es el metodo que me permite agregar elemtos en cualquier ubicacion de mi lista 

lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0,"anthony")


### 3. eliminar elemento de una lista 
python
# metodo pop - es el metodo que elimina el ultimo elemto de una lista es el contrario de append.
 

lista_nombres=["edith","ruth","luz"]
lista_nombres.pop()

# primera manera - metodo remove - este metodo elimina el por el nombre  el elemento que coincida dentro de mi lista 

python

lista_nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")

# segunda opcion - metodo pop - al pasarle por pametro un indice este lo elima de la lista.


lista_nombres=["edith","ruth","luz"]
lista_nombres.pop(0)


# buscar un elemento en una lista 
```python 
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])

pertenecia="edith" in lista-nombres -->


### 5 comparacion de lista 

podemos hacer uso de operadores de comparacion para comparar listas

**Ejem:**

```python 
compara=[1,2,3]<[1,2,4]
# 1 no popr que son iguales en ambas listas 
# 2 no por que son iguales an ambas listas 
# 3 evalua que es menor a 4
# entonces la primera lista es menor que la segunda lista 
print(compara)

### 6. cuidado con las copias 

### 7. FE ERRATAS (Actualizar listas)
```¨python  
lista[1,3,4,5,6]
listaa[0]=2
print(lista)
#[2,3,4,5,6]
#modificando lista con diccionario 
alumnos=[
    (
        "nombre":"anthony",
        "edad":15
    )
    (  
        "nombre":"anthony"
        "edad":29
    )
]
alumnos[0]["edad"]=30
alumnos[0]=("nombre":"mafer","edad"=15)
alumos[1]["sexo"]="por difinir"
print(alumnos)



# crear un programa que reciba una lista desordenada y muestre por terminal la lista ordena y la lista ordena y la lista previa a ser ordena .
lista=[4,76,1,3,6,8,2]
copia_lista=lista.copy()
copia_lista.sort()
print(lista)
print(copia_lista)

# tarea 

# mostrar lista con los 4 diccionarios 
# editar el 3ro registro y cambiarle la edad sin modificar la lista original 
# mostrar la lista original y luego la lista con el registo y cambiarle la edad sin modificar la lista original
# mostrar la lista original y luego la lista con el 3ro registro modificado.

# yo como dueño de si mascota 
# deseo ver una lista de mis mascotas 
# para tomar un resumen o control de ellos ||   

# Lista de mascotas
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
        print(f"Nombre: {mascota['nombre']}, Especie: {mascota['especie']}, Edad: {mascota['edad']}")
    print()

# Llamada a la función para mostrar la lista de mascotas
mostrar_mascotas()

    # yo como dueño de mi mascota 
    # deseo actulizarr la edad de si mascota 
    # para tener un lista correcto de mi mascota 

    # Lista de mascotas
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
        print(f"Nombre: {mascota['nombre']}, Especie: {mascota['especie']}, Edad: {mascota['edad']}")
    print()

# Función para actualizar la edad de una mascota
def actualizar_edad_mascota(nombre_mascota, nueva_edad):
    for mascota in mascotas:
   ♠     if mascota["nombre"] == nombre_mascota:
            mascota["edad"] = nueva_edad
            print(f"Se ha actualizado la edad de {nombre_mascota} a {nueva_edad}.")
            return
    print(f"No se encontró la mascota con el nombre {nombre_mascota}.")

# Llamada a la función para mostrar la lista de mascotas antes de la actualización
mostrar_mascotas()

# Actualizar la edad de una mascota específica
nombre_mascota_a_actualizar = "Luna"
nueva_edad_mascota = 4
actualizar_edad_mascota(nombre_mascota_a_actualizar, nueva_edad_mascota)

# Llamada a la función para mostrar la lista de mascotas después de la actualización
mostrar_mascotas()




#  yo como cordinador 
# habilito la edición de notas para el docente 
# para que pueda actualizar las notas del estudiante  


### 8. listas y diccionarios por compreción 

es una tecnica pythonica que nos permite crear listas y diccionarios en una sola linea conbinadio 
bucles y deciciones 

>[!NOTE]
>**VIC** value loop condicion - valor bucle condicion 
```python
# lista por comprecion
texto="1,4,8,9,6"
neuva_lista=[int(n)for n in texto.split(",")if n%2==0]
print(nueva_lista)

```
```python
# diccionario por comprencion 

lista_amigos("abel","anthony","edith","ruth")
diccionario=()
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)
```