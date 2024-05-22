# controles de flujo
todos los programas trabajan a travez de instrucciones ordenadas.
existen maneras de romper con un flujo normal de los programas creando **bifurcaciones**  o creando **repitición** de instrucciones.
## deciciones
la sentecia de deciciones en python es `if` , en su escritura debemos añadir una **expreción de comparación** terminando con `i` al finall de linea 
### la sentecia if
> ejemplo:

```python 
if true:
    print("es verdad")

## ciclos 
son los controles de flujo que repiten codigo y si sintaxix es 
la sigueiente 
> para FOR:

    python 
#este codigo imprime los numeros 
#del 1 al 10 

for n in range(1,11):
    print(n)
    
almacenar el if en un variable 
``` python  -->
# primer ejemplo if estructurado
edad:int=int(input("escribe tu edad:"))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")
# segundo ejemplo if almacenado en variable
edad:int=int(input("escribe tu edad: "))
rewspuesta:str="eres mayor" if edad>=18 else "eres menor" 
print(respuesta)

> para FOR

for n in range(1,11):
    prin(n)

crear un programa que me imprima las 5 bocales 

vocales= str="aeiou"
for n in range(0,5):
    print(vocales[n])

crear un programa que me muestre los 8 primeros numeros pares

for i in range(1, 17):
    if n % 2 == 0:
        print(n)

crear un programa que me pida al usuario escribir una oracion y mostrar por terminal la cantidad de vocales a que tiene esa oracion 
OJO SOLO LA "a" MINUSCULA

oracion = input("Escribe una oración: ")
contador = 0

for letra in oracion:
    if letra == 'a':
        contador += 1

print(contador)
 
 mismo ejercicio con rangue.
 
oracion = input("Escribe una oración: ")
contador = 0
for n in range(0,len(oracion)):
    if oracion [n]== 'a':
        contador=contador+1
    
        #contador += 1

print(f"la cantidad de letras a que es {contador}")


almacenar el if en un variable 
``` python  -->
# primer ejemplo if estructurado
edad:int=int(input("escribe tu edad:"))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")
# segundo ejemplo if almacenado en variable
edad:int=int(input("escribe tu edad: "))
rewspuesta:str="eres mayor" if edad>=18 else "eres menor" 
print(respuesta)

> para FOR

for n in range(1,11):
    prin(n)

crear un programa que me imprima las 5 bocales 

vocales= str="aeiou"
for n in range(0,5):
    print(vocales[n])

crear un programa que me muestre los 8 primeros numeros pares

for i in range(1, 17):
    if n % 2 == 0:
        print(n)

crear un programa que me pida al usuario escribir una oracion y mostrar por terminal la cantidad de vocales a que tiene esa oracion 
OJO SOLO LA "a" MINUSCULA

oracion = input("Escribe una oración: ")
contador = 0

for letra in oracion:
    if letra == 'a':
        contador += 1

print(contador)
 
 mismo ejercicio con rangue.
 
oracion = input("Escribe una oración: ")
contador = 0
for n in range(0,len(oracion)):
    if oracion [n]== 'a':
        contador=contador+1
    
        #contador += 1

print(f"la cantidad de letras a que es {contador}")


#crear un programa que me cuente  la cantidad de comas y me muestre sus indices.
#ojo: tierne que pedir al usuario.
oracion:str=input("ingrese una oracion: ")
contador:int=0
for indice,letra in enumerate(oracion):
    if letra == ",":
     print(f"su indice es {indice}")
    contador+=1
print(f"la cantidad de comas es {contador}")


oracion:str=input("escribe una oracion: ")
contador:int=0
for n in range(0,len(oracion)):
    if oracion[n]== "a":
        
#escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
#años que ha cumplido (desde 1 hasta su edad)

def
mostrar_anios_cumplidos(edad):
for i in range(1, edad + 1):
    print("Ha cumplido" , i, "años")
#solicitar la edad l usuario 
try:
    edad = int(input("por favor, ingrese su edad: "))
    if edad < 0:
        print("la edad ingresada no es valida. por favor, ingrese un número positivo.")
        else:
    mostrar_anios_cumplidos(edad)
    except valueError:
        print(por favor,ingrese un número entero válido para la edad.")
    
# crear un programa que me pida el nombre de tres personas y guarde en una variable global 
#la ultima letras de sus nombres
#mostrar por pantalla la variable global con las tres ultimas letras del nombre de cada 
#persona 
#ejemplos
#abel
#antony
#edith
#salida lyh

ultims_letra:str=""
for _ in range(3):
    nombre_:str=input("escribe tu nombre: ")
    #ultima_letra+=nombre[-1]
    last_letter:str=nombre[-1]
    ultima_letra+=last_letter
    #ultima_letra=ultima_letra+last_letter
print(ultima_letra)


#crear un programa  que muestre por terminal la 
#siguiente figura:
#a
#ee
#iii
#oooo
#uuuuu


# Mostrar la figura por terminal
print("a")
print("ee")
print("iii")
print("oooo")
print("uuuuu")



