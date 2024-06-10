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
# retorno ("nombre":"jose","edad":45)
```


