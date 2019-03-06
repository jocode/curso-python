# Why python?

* Buen lenguajede programación para principiantes
* Sintaxis clara y código legible
    * Parece pseudocódigo
    * Bueno para aprender a programar
* Una gran cantidad de librerías, simple y divertido
* Usado en muchos contextos
* Usado por importantes compañías
    - Google
    - Yahoo
    - NASA
    - Muchas más
* Es gratis


## What is python

* General purpose programming language
* A high level programming language
* Es de tipado dinámico
* Fun a Easy to learn

> Es como una navaja suiza, lo puedes utilizar para muchas cosas


## Usos

* CLIs
* Aplicaciones web (django)
* Sistemas embedidos
* Aplicaciones de escritorio
* Data Science
* Hacking
* Robots y Hardware
* Inteligencia Artificial


## Instalar python

Vamos a la página oficial de python y le damos descargar. Luego de descargarlo lo instalamos y seleccionamos la opción de agregar variable de entorno al SO

**Algunos editores de código que podemos utilizar son:**

* Atom
* Sublime Text
* Visual Studio Code


> Los archivos de python tienen la extensión `.py`


## Hola Mundo

Podemos ejecutar esto desde la terminal ejecutando el comando `python`. Al hacer eso se nos abrirá una consola interactiva de python y podremos coloar el siguiente texto

```python
print('Hola mundo')
```

## Comentarios

Los comentarios son herramientas que tenemos para describir el código. Al colocar un comentario el  intérprete ignora eso y no lo ejecuta

* Comentario de una sola línea

```python
# Comentario de unsa sola línea
```

* Comentarios multilínea

```python
"""
Este es un comentario de varias lineas
Inicia con tres comillas y 
finaliza con tres comillas 
"""
```


## Tipos de datos

- **str** Strings
- **int** Enteros
- **float** Flotantes
- **None** Se utiliza para indicar que no tiene tipo de dato asignado

con **del** eliminamos los valores de una variable

* Convensiones para el nombrado de variables

```python
book_name = "Hi" # Snake Case
bookName = "Other" # Camel Case
BookName = "High" # Pascal Case
```

Las constantes en python se declarar con **MAYÚSCULAS** por convención


## Métodos para Strings

El método dir(), muestra los métodos que tienen un determinado tipo de dato

```python
myStr = "Hello World"
print(dir(myStr))
```

Algunos de los métodos en python son:

- **upper()** Convierte el texto a mayusculas
- **lower()** Convierte el texto a minusculas
- **swapcase()** Deja todas las palabras en mayusculas exepto la primera letra de cada palabra
- **capitalize()** Convierte la primera letra de texto en mayuscula
- **replace(find, replace)** Busca las coincidencias del primer parámetro y las reemplaza con el segundo
- **count('j')** Cuenta la cantidad de caracteres especificados
- **startswith('value')** Indica si es verdadero o falso dada el argumento indicado
- **endswith('value')** Indica si la palabra termina con la letra o valor ingresado por parámetro
- **split(' ')** Separa un strings en una lista, a partir de un caracter especificado
- **find('value')** Busca la posición del parámetro especificado 
- **isnumeric()** Devuelve verdadero o falso si el valor es numerico
- **isalpha()** Devuelve verdadero o falso si el valor es alfanumerico

- **len()**

```python
myStr = "Hello world"
print(myStr.upper())
print(myStr.count('l'))

print(len(myStr)) # Muestra el tamaño de la variable (En caracteres)

print(myStr[6]) # Muestra la letra 'w'
print(myStr[-1]) # Muestra el último caracter 'd'
```

## Listas

- **append('elemento')** Agrega un elemento al ultimo lists

- **extend(['hola', 'mundo'])** Agrega una lista de elementos una por una a la lista

- **insert(posicion, 'valor')**  Ingresa un elemento dada una posicion

- **pop(1)** Elimina el ultimo elemento de la lista, o si le paso el indice como argumento me elimina ese argumento

- **remove('color')** Elimina el elemento que contenga el valor 'color'

- **sort()** Ordena de manera ascendente los elementos

- **sort(reverse=True)** Ordena de manera descendente los elementos de la lista

- **clear()** Elimina todos los elementos de la lista

- **index('blue')** Devuelve el índice que coincida con el primer valor de blue

- **count('pink')** Cuenta los elementos que tengan ese valor

```python
colors = ['yellow', 'blue', 'red', 'pink']
colors.append('gray')
print(colors.sort())
```

## Tuplas

Definen un conjunto de elementos que no se pueden cambiar, que son inmutables. Son más rápidas que las listas

```python
x = (1,2,3,4)
months = ('Eneero', 'Febrero')
print(dir(months))
```

La coma, es importante, porque si definimos una solo elemento en la tupla sin la coma, lo tomará como otro tipo de dato

> Las tuplas no soportan la reasignación


## Set

Es una colección que no tienen índices

```python
colors = {'Red', 'Green', 'Blue'}
print(colors)
print('Red' in colors)
colors.add('Yellow')
print(colors)
print.remove('Red')
print(colors)

colors.clear()
```


## Diccionarios

Son un conjunto de datos que podemos organizarlos por claves y valores

```python
product= {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

print(product)
print(dir(product))

print(products.keys()) # Devuelve las claves del diccionario
print(products.items()) # Devulve cada uno de los elementos como una lista
```

> Siempre las claves vas con comillas


## Funciones `lambda`

Son funciones anónimas que un numero de argumentos pero se escriben en una sóla linea 

```python
suma = lambda numberOne, numberTwo : numberOne + numberTwo

print(suma(10, 30))
```


## Módulos

Hay tres tipos de módulos en python  

* Los módulosde python
* Modulos de terceras partes
* Propios modulos


Por ejemplo el módulo **datetime** permite ver la fecha del sistema

*Para ver los módulos que tiene el lenguaje, buscar python modules*

```python
from datetime import date

today = date.today()
print(today) 
```

Para utilizar módulos de terceros podemos acceder a [PyPI](https://pypi.org/) y descargarlos para usarlos en nuestros proyectos

* Flask
* Django
* Tkinter

