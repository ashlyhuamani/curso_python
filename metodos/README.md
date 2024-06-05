# METODOS EN PYTHON   
##  NUMEROS 
```python
len (154788
# devuelve la cantidad de caracteres
# el espacio cuenta tambien como carecter
# 10 
```
## TEXTOS 
```python 
len(["h","o","," ";a"])
# devueleve la cantidad de elementos 
# el espacio cuanta tambien como un caracter
# 4
```
## tuplas 

count(): Este método devuelve el número de veces que un elemento específico aparece en la tupla.
index(): Devuelve el índice de la primera aparición de un elemento específico en la tupla.

```python
mi_tupla = (1, 2, 3, 4, 2, 5, 2)

# Utilizar el método count() para contar el número de veces que aparece el número 2 en la tupla
apariciones_2 = mi_tupla.count(2)
print(f"El número 2 aparece {apariciones_2} veces en la tupla.")

# Utilizar el método index() para obtener el índice de la primera aparición del número 4 en la tupla
indice_4 = mi_tupla.index(4)
print(f"El índice de la primera aparición del número 4 es: {indice_4}")

```
## diccionario s

- keys(): Devuelve una lista con todas las claves del diccionario.
- values(): Devuelve una lista con todos los valores del diccionario.
- items(): Devuelve una lista de tuplas (clave, valor) del diccionario.
- get(): Devuelve el valor asociado a una clave específica del diccionario. Si la clave no existe, se puede proporcionar un valor - predeterminado para que se devuelva en su lugar.
- pop(): Elimina y devuelve el valor asociado a una clave específica del diccionario.
- popitem(): Elimina y devuelve un par clave-valor aleatorio del diccionario.
- update(): Agrega pares clave-valor al diccionario o actualiza los valores existentes con nuevos valores.

```python
# Definir un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Utilizar el método keys() para obtener todas las claves del diccionario
claves = mi_diccionario.keys()
print("Claves del diccionario:", claves)

# Utilizar el método values() para obtener todos los valores del diccionario
valores = mi_diccionario.values()
print("Valores del diccionario:", valores)

# Utilizar el método items() para obtener todas las tuplas (clave, valor) del diccionario
items = mi_diccionario.items()
print("Pares clave-valor del diccionario:", items)

# Utilizar el método get() para obtener el valor asociado a una clave específica
edad = mi_diccionario.get("edad")
print("Edad:", edad)

# Utilizar el método pop() para eliminar y obtener el valor asociado a una clave específica
ciudad = mi_diccionario.pop("ciudad")
print("Ciudad:", ciudad)

# Utilizar el método update() para agregar nuevos pares clave-valor al diccionario
mi_diccionario.update({"profesion": "Ingeniero", "edad": 31})
print("Diccionario actualizado:", mi_diccionario)
```

