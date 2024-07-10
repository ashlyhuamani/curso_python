# Averiguar modulos y paquetes en python 
**modulo:**
es un conjunto de funciones 
un archivo `py` con funciones 

**paquete:**
es una carpeta con una serie de archivos `py`
una carpeta con modulos de python

En Python, los módulos son archivos que contienen definiciones y declaraciones de Python. Un módulo puede definir funciones, clases y variables, y puede incluir instrucciones ejecutables. Por otro lado, los paquetes son directorios que contienen uno o más módulos y un archivo especial llamado __init__.py.

### **Módulos:**

Creación de un módulo:

Supongamos que tienes un archivo llamado mimodulo.py que contiene una función simple:
``` python
# mimodulo.py
def saludar(nombre):
    return f"Hola, {nombre}!"
```
### **1.- Uso de un módulo:**
Puedes importar y utilizar este módulo en otro archivo de la siguiente manera:
```python
import mimodulo

mensaje = mimodulo.saludar("Juan")
print(mensaje)  # Output: Hola, Juan!
```
### **Paquetes:**

**1. Estructura de un paquete:**

  Supongamos que tienes una estructura de directorios como esta:
```python
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
```
**1. Contenido de los módulos en el paquete:**
   
En modulo1.py:
```python
# modulo1.py
def suma(a, b):
    return a + b
```
En modulo2.py:
```python 
# modulo2.py
def resta(a, b):
    return a - b
```
**3. Uso de un paquete:** 

Puedes importar y utilizar los módulos de un paquete de la siguiente manera:
```python 
from mi_paquete import modulo1, modulo2

resultado_suma = modulo1.suma(5, 3)
resultado_resta = modulo2.resta(10, 4)

print(resultado_suma)  # Output: 8
print(resultado_resta)  # Output: 6
```
Con esta estructura, mi_paquete es un paquete de Python que contiene los módulos modulo1 y modulo2, y puedes importar y utilizar las funciones definidas en esos módulos.
Los módulos y paquetes son fundamentales en Python para organizar y reutilizar código de manera efectiva. 

# Diferencias entre modulos y paquetes 

### **Módulos:**

**1. Definición:**

+ Un módulo en Python es un archivo individual que contiene código Python. Puede incluir funciones, clases, variables y declaraciones ejecutables.
+ Los módulos son utilizados para organizar y reutilizar código de manera efectiva.

**2. Uso:** 

+ Se importan en otros scripts o módulos utilizando la declaración import.
+ Se pueden crear módulos simples para tareas específicas y luego reutilizarlos en diferentes partes de un proyecto.

### **Paquetes:**

**Definición:**

+ Un paquete en Python es un directorio que contiene uno o más módulos y un archivo especial __init__.py. Este archivo indica que el directorio debe ser tratado como un paquete.

+ Los paquetes permiten organizar y estructurar el código de Python de manera jerárquica.

**Estructura:**

+ Un paquete es un conjunto de módulos organizados en un directorio. Puede contener subpaquetes y módulos que se pueden importar y utilizar de manera similar a los módulos individuales.
  
### **Diferencias Clave:**

**Módulos:**

+ Son archivos individuales que contienen código Python.
+ Se utilizan para organizar y reutilizar funciones, clases y variables.
+ Se importan con la declaración import.
  
**Paquetes:**

+ Son directorios que contienen módulos y un archivo __init__.py.
+ Permiten organizar y estructurar el código de manera jerárquica.
+ Pueden contener subpaquetes y módulos.
  
**Ejemplo:**

+ Supongamos que tenemos un módulo llamado operaciones.py que contiene funciones matemáticas.
+ Creamos un paquete llamado matematicas que contiene los módulos operaciones.py, estadisticas.py, etc.
  
### Uso de Módulo y Paquete:
```python
# Uso de un módulo
import operaciones
suma = operaciones.sumar(5, 3)

# Uso de un paquete
from matematicas import estadisticas
promedio = estadisticas.calcular_promedio([4, 5, 6, 7])
```
**Resumen:**

* Los módulos son archivos individuales que contienen código Python, mientras que los paquetes son directorios que contienen módulos y un archivo __init__.py.
+ Los módulos permiten organizar y reutilizar código a nivel de archivo, mientras que los paquetes permiten organizar y estructurar el código de manera jerárquica en directorios.