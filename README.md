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

Para mostrar los consejos que se tienen para escribir bueno programas, lo podemos mostrar al colocar en la terminal de python `import this`. 


## Estructura de datos

### Listas

* Una lista es una secuencia de elementos
* Cuando se asigna a una variable, permite agrupar varios elementos en un sólo lugar
* Se crar con corchetes **[]** on con la keyword **list**
* Las listas son mutables

```python
supermercado = ['apio', 'tomate', 'queso']
otraLista = list() # Crea una lista vacía
# Se accede mediante el indice
supermercado[0]

# el método append agrega un elemento a la lista
otraLista.append('Esteban')
# Eliminar un elemento dado un valor
otraLista.remove('apio')
```


### Diccionarios en pyhton

Un diccionario es como una generalización de una lista
* Un diccionario es un mapa de llaves y valores. Los valores pueden ser de cualquier tipo
* Se crea con llaves {} o con el  keyword **dict**

Por ejemplo
```python
mi_other_dict = dict()
mi_dict = {}
mi_dict['clave'] = 'valor'
```

También se pueden añadir valores al momento de inicializarlo
```python
mi_dict = {'clave': 'valor'}
```

Para ver más información sobre esto, ver el archivo [Estructuras de Datos
](estructuras-datos.py)


**Para más información sobre el lenguage ver los archivos**

* [Uso de strings y Ciclos](string-y-ciclos/readme.md)

* [Estructuras de Datos](estructuras-datos/readme.md)

* [Uso de objetos y módulos](uso-objetos-modulos/readme.md)

* [Why python?](complementos/readme.md)

* [Python en Servidor web](aplicacion-web/readme.md)

* [Sitio web con Python](website/readme.md)


## Envío de Emails con Python 

Para enviar correos electrónicos con python mediante gmail, debemos habilitar la opción de **Acceso de apps menos seguras** en la configuración de la cuenta en *seguridad->Acceso de apps menos seguras->Permitir el acceso de aplicaciones menos seguras (ON)*, de esta forma la aplicación en python podrá enviar correos a través de la cuenta.

Python ya cuenta con una librería para el envío de correos, y se llama **smtplib**, los correos se enviarán medianteel protocolo **SMTP** (Simple Mail Transfer Protocol)

- Librería **python-decouple**, permite hacer uso de variables de entornos