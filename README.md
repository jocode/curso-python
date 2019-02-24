## ¿Por qué python?

Es un lenguaje con una sintaxis muy sencilla, se lee y se ejecuta casi como se escribe, además tiene una gran comunidad detrás.

> Programar es darle instrucciones a la máquina

Los lenguajes se componen en piezas básicas, como bloques de construcción.

- Hola mundo en python 

Instalar python si no está instalado, y ejecutar en el terminal el comando python
```python 
print("Hola mundo");
```

## ¿Qué es un Programa?

Un programa es una secuencia de instrucciones que especifican cómo realizar un computo.

Todos los programas se componen de "partes" básicas que se utilizan para crear "partes" más complejas.

* Input, Output, Estructuras de datos, Condicionales, Iteraciones y matemáticas.

### Primer programa

Usamos la librería turtle para dibujar un cuadrado. Está en el archivo [ejemplo](ejemplo.py)

> Si se está trabajando en linux, es necesario instalar la librería **python-tk**  usando el siguiente comando `sudo apt-get install python-tk`, de no ser instalado el programa no funcionará

Si está instalado, luego debemos ejecutar el archivo colocandonos en la carpeta donde se encuentra, y escibir el comando `python ejemplo.py`

## Operadores matemáticos

Nos permiten trabajar y generar nuevos valores. Los operadores vienen de las matemáticas 
* Suma						__\+__
* Resta 					__\-__
* Multiplicación 			__\*__
* División 					__/__
* División de enteros 		__//__ 
* Residuo de la división 	__%__
* Potencia de un número 	__**__


## Tipos de Datos 

El orden de las operaciones son:
* Paréntesis
* Exponentes
* Multiplicación / División
* Adición / Sustración

Los valores son uno de los componentes básicos con los que trabaja un programa, como una letra o un número.

* Los valores tienen un tipo

* Los tipos de básios son
	- Integer <int>
	- Float <float>
	- String <str>
	- Boolean <bool>

Con la función **type( args )** podemos saber qué tipo de datos es el valor que se le pasa por parámetro

```python
type(3.1416)
```

## Declaración de variables y expresiones

* Las expresiones se componen de valores conectados por operadores
* Cuando la computadora evalúa la expresión, el resultad es otro valor 
* Los valores pueden guardarse en variables
* Las variables se pueden reasignar

**Variable** Es un contenedor de valores

Las variables, tienen algunas condiciones 
- Deben ser nombres significativos
- Relacionar con lo que representa la variable 
- No deben ser Keywords (Palabras reservadas)


## Funciones

* Una función es una secuencia de comandos que realizan un cómputo.
* Para definirla se utiliza el keyword **def** se le asigna un nombre y se define la secuencia de comandos 
* Las funciones son llamadas por su nombre y regresan un resultado
* Pueden recibir cero o más parámetros 

```python 
''' Declaración de la funcion '''
def suma(a, b)
	return a+b

'''LLamada a la funcion'''
suma(5, 2)
```

Cuando declaramos una función con el mismo nombre de una variable, entrará en conflicto y se colocará cono funcion (**def**)


## Indicar a python qué función iniciar

Para indicarle a python con qué función iniciar, debemos usar la siguiente sentencia 

```python
if __name__ == '__main__':
	run() # Función que se llama
```

## scope de funciones

Las variables existen únicamente cuando el contenedor existe. Por ejemplo si tengo definida una variable en una funcion, sólo existirá para esa función. No puedo llamarla desde otra.

## Estructuras de Condicionales

- Una expresion booleana se evalúa como verdadera o falsa (True, False)
- Operadores relacionales
	- ==
	- !=
	- > 
	- >=
	- <
	- <=
- Operadores lógicos
	- and
	- or
	- not

Python es sensible a mayúsculas y minúsculas en los caracteres

Por ejemplo:
```python
'z'>'a' # True
15 != 10 # True
```

Las expresiones boolenas son las que se evalúan como verdaderas o falsas.

```python
def say_hello(age):
	if age > 18:
		print('Hola Senior')
	else 
		print('Hola nino')
```

**pass** es un key de python para indicarle que no tiene definido nada aún, pero que en algún momento de define. Si no se coloca pass, python generará un error porque no sabe cuando empieza o termina la funcion

*[Calcular si un número es primo](numeros_primos.py)*

Un condicinal puede tener condiciones anidadas dentro de cada una.


## Para ver el Zen de python

Para mostrar los consejos que se tienen para escribir bueno programas, lo podemos mostrar al colocar en la terminal de python `import this`. Con esta líena nos mostrará la filosofía que se debería seguir para construir un software excelente. Lo que dice el lo siguiente:

>Beautiful is better than ugly.

>Explicit is better than implicit.

>Simple is better than complex.

>Complex is better than complicated.

>Flat is better than nested.

>Sparse is better than dense.

>Readability counts.

>Special cases aren't special enough to break the rules.

>Although practicality beats purity.

>Errors should never pass silently.

>Unless explicitly silenced.

>In the face of ambiguity, refuse the temptation to guess.

>There should be one-- and preferably only one --obvious way to do it.

>Although that way may not be obvious at first unless you're Dutch.

>Now is better than never.

>Although never is often better than right now.

>If the implementation is hard to explain, it's a bad idea.

>If the implementation is easy to explain, it may be a good idea.

>Namespaces are one honking great idea -- let's do more of those!