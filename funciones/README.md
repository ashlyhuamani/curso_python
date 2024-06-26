# FUNCIONES 
Matematicamente es una operación que toma una o mas valores llamados `argumentos`y produce un valor denominado `resultado`.
> [!NOTE]
> Todos los lenguajes de programación tiene funcionés incorporadas (`funciones internas`),y funciones creadas por el usuario (`funciones externas○`).
En programacion una funcion es un subprograma, es una estructura que nos permite agrupar codigo y sus principales objeptivos o son:

* `NO REPETIR` fragmentos de codigo
* `REUTILIZAR` el codigo en distintod escenarios 

## ESTRUCTURA DE UNA FUNCION 
Una funcion viene `definida`por un `nombre`, sus `parametros` y su valor de `retorno`.
Una ves creada la funcion podremos solicitar su ejecucion `invocado`la funcion por su `nombre`.
## DIFINIR UNA FUNCION EN PYTHON 
Para definir una funcion en python primero utilizaremos la palabra reserrvada `def` seguida por el `nombre`de la funcion.  A continuacion especificaremos los  `parametros`con `()` si es un funcion sin parametros,`(a)`si es funcion con parametros, si se tuviera mas de un parametros iran separados por `,`, finalizaremos la linea con `:` , en la siguiente linea sin olvidar el identado, comenzara el `cuerpo` de la funcion (micro programa) que puede contener 1 o mas sentacias, finalmente devera `retornar` un resultado con la palabra reserbada`return`.

> [!TIP]
> * OBSERVACION 
> print:dentro de una funcion una herramienta para comprabar que una funcion esta cumpliendo una tarea correcta.
>* Como retorno tambien se puede utilizar la `funcion interna`,`print ()`, para depuracion de codigo no es recomendable usarlo en produccion.

**Ejemplo:**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return f"(saludo), (saludo_dos)"
    #print(f"(saludo), (saludo_dos)")
print(saludo())
#saludo
```
## Invocar una funcion
Para invocar, (o llamar, ejecutar)una funcion solo tendremos que escribir el `nombre` de la funcion seguidapor`()` parentisis.
```python
def saludo():
    print("hola")
#invocando la funcion 
saludo()
```
## Retornar un valor 
Las funciones pueden retornar (o devolver) un valor.
```python
def uno():
    return 1
uno()
```
> [!WARNIING]
> No confundir `print()` con `return`. el valor retornado por `return` nos permite usarlo fuera de su contexto. y `print()` solo mostrara el literal por terminal.
> **ejemplo**
> en el archivo `lecture.py`

## Retornando multiples valores
El secreto es hacerlo mediante un tipo de dato estructurado 
```python
def varios():
    return 2,3,4
varios()
#return ["hola",45]
def dicc():
    return ("nombre":"jose","edad":45)
dicc()
# retorna ("nombre":"jose","edad":45)
```
## Parametros y Argumentos 
si una funcion dispusiera de valores de entrada estaria limitada en su actuacion, es por ello qu los `parametros`no permiten variar los datos que consume una funcion para obtener destintos resutados.

**Ejemplos:**

*crear una funcion que recibe un valor numerico y retorna su raiz cuadrada*
```python
def sprt(valor):
    return valor**(1/2)
# NOTA: es un caso, el valor 4 es un argumento de la funcion
sqrt(4)
```
Cuando llamamos a un funcion con `argumentos`, los valores de estos argumentos se copian en los correspondiente `parametros` dentro de la funcion.
```python 
def ejem(a,b,c):
    return a+b+c
ejm(4,5,6)
```
### Argumentos nominales 
En esta aproximacion los argumentos no son copiados en un orden especifico si no que **se asignan por nombre a cada parametro**, Ello nos permite evitar el problema de conocer o reconcer cual es el orden del parametros en la difinicion de la funcion.
Para utilizarlo, basta realizar una asignicion de cada argumento en la propia llamada funcion.

**Ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia (familia),
    con (num_core)cores y con una frecuencia 
    de (frecuencia)
    """)
# haciendo uso de argumentos nominales 
buil_cpu(nue_core=4,familia="intel",frecuencia=2.7)
```
### Argumentos posicionales 
Los argumentos son copiados en un orden especifico, en este caso debemos conocer o recortar cual es el orden de los parametros 
***Ejemplos:***
```python
def buil_cpu(familia,num_core,freccuencia):
    print(f"""
    la cpu es de la familia (familia),
    con(num_core)cores y con una 
    frecuencia de (frecuencia)
    """)
# haciendo uso de argumentos pisicionales 
buil_cpu("intel",4,2,7)
```
### Parametros por defecto 
Es posible espesificar **valores por defectos** en los parametros en una función, en el caso de que no se proporcione un valor en el argumento en la llamada a la funcion, el parametro correspondiente tomara un valor difinido por defecto. 
***Ejemplo:***
```python
def alumno(nom,app,estado="aprobado"):

alumnos("ruth","castillo")
alumno("anthony";"crucez","desaprobado"
)
```
### Desempaquetados/Empaquetado de argumetos(tarea)
Desempaquetar y empaquetar argumentos son conceptos comunes en programacion, especialmente en lenguajes como python.

***- Empaquetar argumentos*** : consiste en agrupar múltiples argumentos en una sola variable para pasarlos a una función de manera más conveniente.Por ejemplo, en Python, se pueden empaquetar argumentos en una tupla o un diccionario y luego pasar una estructura de datos a una función.

***- Desempaquetar argumentos*** : Por otro lado, desempaquetar argumentos significa tomar una estructura de datos que contiene múltiples valores (como una dupla o un diccionario) y pasar esos valores como argumentos individuales a una función. Esto es útil cuando se nesecita pasar múltiples argumentos a una función que espera argumentos separados.

En python,el desempaquetado de argumentos se puede realizar utilizando el operador  `* ` para desempaquetar una tupla o una lista, o ` ** ` para desempaquetar un diccionario.
 
Por ejemplo, en Python, si tenemos una función que espera tres argumentos  `funcion(a, b, c)` , y tenemos una tupla con esos valores ` (1, 2, 3)` , podemos desempaquetar los valores de la tupla y pasarlos como argumentos a la función de la siguiente manera:  funcion(*tupla) .

### Funciones internas python(tarea) 
Python tiene una variedad de funciones internas (built-in functions) que están disponibles para su uso sin necesidad de importar módulos adicionales. Aquí tienes algunos ejemplos de funciones internas de Python:

print(): Imprime un mensaje en la consola o en la salida estándar.
* len(): Devuelve la longitud de un objeto, como una cadena, lista o diccionario.
* type(): Devuelve el tipo de un objeto.
* input(): Lee una zentrada del usuario desde la consola.
* range(): Genera una secuencia de números dentro de un rango especificado.
* int(): Convierte un valor en un entero.
* float(): Convierte un valor en un número de punto flotante.
* str(): Convierte un valor en una cadena.
* list(): Convierte un objeto iterable en una lista.
* dict(): Crea un nuevo diccionario.

Estas son solo algunas de las funciones internas más comunes en Python, pero hay muchas más disponibles. Puedes encontrar una lista completa de las funciones internas de Python en la documentación oficial de Python.
Recuerda que las funciones internas son parte del lenguaje Python y están disponibles para su uso directo sin necesidad de importar módulos adicionales.

## Tipos de funciones 
### funciones anonimas (funciones lambda)
una funcion no tiene nombre
`lambad:"hola"`

### funciones closure
una funcion que dentro tiene otra funcion
`def saludo(nombre):
 print(f"bienvenido (nombre)")`
### funciones callback
funciones que reciben por parametro otra funcion
`int(input("ingrese un numero"))`
### Programacion funcion
la programacion funcional no requiere y que sepas como desarrollador y ejecuta el procesamiento de la informacion.

**ejemplos:**
```python
# programcion interativa
lista=[5,7,8,4,1]
del num_minimo(1):
    minimo=1[0]
    for n in 1:
        if n < minimo:
            minimo=n
    return minimo
#programacion funcional 
min(lista)
```
#### AVERIGUAR SOBRE MAP(), FILTER(), REDUCE() (tarea)
**`MAP():`**

La función **map()** en Python es una función integrada que se utiliza para aplicar una función dada a cada elemento de un iterable (como una lista, tupla, etc.) y devuelve un iterador que contiene los resultados. La sintaxis general de la función map() es la siguiente :
```python
map(funcion, iterable)
```
* funcion: Es la función que se aplicará a cada elemento del iterable.
* iterable: Es el iterable (lista, tupla, etc.) al que se aplicará la función.
  
Aquí tienes un ejemplo básico de cómo se utiliza la función map():
```python
# Definir una función para duplicar un número
def duplicar(x):
    return x * 2

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Utilizar la función map() para duplicar cada número en la lista
resultado = map(duplicar, numeros)

# Convertir el resultado a una lista
resultado_lista = list(resultado)

print(resultado_lista)  # Output: [2, 4, 6, 8, 10]
```
En este ejemplo, la función duplicar(x) duplica un número dado. Luego, utilizamos la función map() para aplicar la función duplicar a cada elemento de la lista numeros. El resultado es un iterador que contiene los números duplicados. Al convertir este iterador en una lista, obtenemos una lista con los números duplicados.

**`FILTER()`**

La función `filter()` en Python es una función integrada que se utiliza para filtrar elementos de un iterable (como una lista, tupla, etc.) según una función de filtro dada. La función `filter()` devuelve un iterador que contiene los elementos para los cuales la función de filtro devuelve True. La sintaxis general de la función filter() es la siguiente:

```python
filter(funcion_filtro, iterable)
```
* funcion_filtro: Es la función que se utiliza para evaluar cada elemento del iterable. Debe devolver True o False.
* iterable: Es el iterable (lista, tupla, etc.) del cual se desean filtrar los elementos.
* 
Aquí tienes un ejemplo básico de cómo se utiliza la función filter():

```python
# Definir una función para filtrar números pares
def es_par(x):
    return x % 2 == 0

# Crear una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utilizar la función filter() para filtrar los números pares de la lista
resultado = filter(es_par, numeros)

# Convertir el resultado a una lista
numeros_pares = list(resultado)

print(numeros_pares)  # Output: [2, 4, 6, 8, 10]
```
En este ejemplo, la función es_par(x) evalúa si un número dado es par. Luego, utilizamos la función filter() para filtrar los números pares de la lista numeros. El resultado es un iterador que contiene solo los números pares. Al convertir este iterador en una lista, obtenemos una lista con los números pares.


La función filter() es útil cuando se desea filtrar elementos de un iterable basado en una condición específica.

 Puede ser utilizada en combinación con funciones lambda para operaciones de filtrado rápidas y eficientes.

**`REDUCE()`**

La función `reduce()` en Python se encuentra en el módulo functools y se utiliza para aplicar una función de manera acumulativa a los elementos de un iterable, de izquierda a derecha, de manera que los elementos se reducen a un solo valor. La función `reduce()` requiere al menos dos argumentos: la función a aplicar y el iterable sobre el cual se aplicará la función. La sintaxis general de la función `reduce()` es la siguiente:
```python
functools.reduce(funcion, iterable)
```
* funcion: Es la función que se aplica de manera acumulativa a los elementos del iterable.
* iterable: Es el iterable (lista, tupla, etc.) sobre el cual se aplicará la función de reducción.
  
Es importante tener en cuenta que a partir de Python 3, la función `reduce()` se ha movido al módulo functools, por lo que primero debes importarla antes de poder utilizarla.

 Aquí tienes un ejemplo básico de cómo se utiliza la función `reduce()` para encontrar el producto de una lista de números:
 ```python
 from functools import reduce

# Definir una función para multiplicar dos números
def multiplicar(x, y):
    return x * y

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Utilizar la función reduce() para encontrar el producto de los números
resultado = reduce(multiplicar, numeros)

print(resultado)  # Output: 120 (1 * 2 * 3 * 4 * 5)
```
En este ejemplo, la función `multiplicar(x, y)` se utiliza para multiplicar dos números. Luego, utilizamos la función `reduce()` para aplicar esta función de manera acumulativa a los elementos de la lista numeros, lo que nos permite encontrar el producto de todos los números en la lista.

La función `reduce()` es útil cuando se desea realizar operaciones acumulativas en una secuencia de elementos y reducirlos a un solo valor. Puede ser una herramienta poderosa para ciertas operaciones matemáticas y de reducción de datos.