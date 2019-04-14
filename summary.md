# Conceptos Básicos sobre Python

## ¿Qué es Python?

Python es un lenguaje de programación creado por **Guido Van Rossum**, con una sintaxis muy limpia, ideada para enseñar a la gente a programar bien. Se trata de un lenguaje interpretado o de *script*

- **Ventajas**
    * __Legible__ Sintaxis intuitiva y estricta
    * __Productivo__ Ahorra mucho código
    * __Portable__ Para todo sistema operativo
    * __Recargado__ Viene con muchas librerías por defecto


Editores en los que se puede escribir: Visual Studio Code, Atom o Sublime

## Instalación

Tal vez sabes que existen dos versiones de Python que tienen un gran uso actualmente, *Pyhton 2.x* y *Pyhton 3.x*, se pueden utilizar cualquiera de las dos, pero se recomienda usar la version 3.x

Para instalar Python sólo debes seguir los pasos dependiendo del sistema operativo instalado en el ordenador

### Windows

Para instalarlo en Windows, debemos ir a https://www.python.org/downloads/, el sitio reconocerá el sistema operativo y dará las opciones para descargar.

Ejecuta el archivo que descargaste y sigue los pasos de instalación. Al finalizar vas a poder utilizar Python en tu computador y estás listo para continuar con el curso.


### MacOS

La forma sencilla es tener instalado **homebrew** y usar el comando:

- Versión 2.7
`brew install python`

- Versión 3.x
`brew install python3`


### Linux

En Linux es muy posible que esté instalado. Para comprobarlo podemos ejecutar siguiente comando en la terminal

- Versión 2.7
`python -V`

- Versión 3.x
`python3 -V`

Si el comando arroja un error quiere decir que no lo tienes instalado. En ese caso los pasos para instalarlo van a cambiar según la distribución que tengas instalada, pero en general el gestor de paquetes de la distribución debe tener el paquete o puedes descargar los archivos para instalarlo manualmente.


## Antes de empezar

Para usar Python debemos tener un editor de texto abierto y una terminal o cmd (Línea de comandos en windows) como administrador.

No le tengas miedo a la consola, la consola es tu amiga.

Para ejecutar Python abres terminal y escribes.

- `python`

Se le abrirá una consola de Python, lo notarpas porque el prompt cambia:
- `>>>`

En esta puedes usar todos los comandos de Python o escribir código directamente.

> Si deseas ejecutar código de un archivo sólo debes guardarlo con `extension.py` y luego ejecutar en la terminal

- `$ python archivo.py`

Ten en cuenta que debes estar en la carpeta en donde se ubica el archivo.

Cuando usamos Python debemos atender ciertas reglas de la comunidad para definir su estructura. Las encuentras en el libro **PEP8**


## Tipos de datos en Python

- **Enteros (int)** Todos los números, enteros y long

*Por ejemplo: 1, 2.3, 2121, 345213, -124*

- **Booleanos (bool)** Son los valores falso o verdadero, igual compatibles con todas las operaciones boolenanas (and, not, or)

*Ejemplo: True, False*

- **Cadenas (str)** Son cadenas de texto

*Ejemplo: "Hola", "¿Cómo estas?"*

- **Listas** Son un grupo o array de datos, puede contener cualquiera de los datos anteriores:

*Ejemplo: [1,2,3,"Hola",[2,5,2],[1,"Buenas",True]]*

- **Diccionarios** Son un grupo de datos que se acceden a partir de una clave

*Ejemplo: {"clave":"valor"},{"nombre":"Fernando"}*

- **Tuplas** Es un grupo de datos que se diferencias de la lista en que, ésta después de creada, no se puede modificar

*Ejemplos: [1,2,3,"hola",[1,2,4]],[1,["Hola",True]]  Pero jamás podremos cambiar los elementos de esa Tupla*


En Python trabajas con **módulos y ficheros** que usas para importar las librerías.


## Funciones

Las funciones se definen usando la palabra clave **def** junto a un nombre y parantesis que reciben los argumentos a usar. Esa instrucción termina con dos puntos (:)

Después por indentación colocas los datos que se ejecutarán desde la función

```python
def miFuncion():
    return "Hola, soy una función"

miFuncion() # Devolverá Hola, soy una función 
```

## Variables

Las variables, a diferencia de los demás lenguajes de programación, no debes definirlas, ni tampoco su tipo de dato, ya que al momento de iterarlas se identificará su tipo. Recuerda que en Python todo es un objeto

```python
A = 3
B = 6
C = "Mi nombre"
``` 

## Listas

Las listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato

```python
listas = [22, True, "Holala", [2,5]]
print(listas[2]) # Mostrará Holala
``` 

## Tuplas

Las tuplas tienen el mismo formato de las listas, sin embargo no puedes editar los datos de una tupla después de que la has creado

```python
tuplas = (22, True, "tupla", (2,5))
print(tuplas[0]) # Mostrará 22
``` 

## Diccionarios

En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cuál accederás con la llave

```python
diccionario = {"key":"value", "nombre": "Johan", "username":"jocode"}
print(diccionario["nombre"]) # Mostrará Johan
```

## Conversiones de tipos de Datos

- De flotante a entero
`int(4.3) # Mostrará 4`

- De entero a flotante
`float(4) # Mostrará 4.0`

- De entero a string
`str(4.3) # Mostrará "4.3"`

- De tupla a lista
```python
list((4,5,2))
[4,5,2]
``` 


## Operadores Comunes

- Longitud de una cadena, lista, tupla, etc.
`len("key")     # 3`

- Tipo de dato
`type(4)    # type int`

- Aplicar una conversión a un conjunto como lista
```python
map( str, [1, 2, 3, 4])
['1', '2', '3', '4']
```

- Redondear un flotante con x números de decimales
`round(6.3243, 1)   # 6.3`

- Generar un rango en una lista (esto es mágico)
```python
range(5)
[0,1,2,3,4]
```

- Sumar un conjunto
`sum([1,2,4])   # 7`

- Organizar un conjunto
`soted([5,6,2])     # [2,5,6]`

- Decir qué le puedes aplicar a x tipos de datos
```python
dir([5,2,1])
# (Aparecerá todas las funciones que tiene una lista)
```

- Información sobre una función o librería
```python
help(sorted)
# (Aparecerá la documentación de la función sorted)
```


## Clases

Las clases son uno de los conceptos con más definiciones en la programació, pro en resumen son sólo una representación de un objeto. Para definir la clase se usa la palabra resevada **class** y el nombre. En caso detener parámetros se colocan entre paréntesis.

Para crear un constructor se define una función dentro de la clase con el nombre **__init__** y de parámetro *self* (Significa su clase misma), y los argumentos que recibirá

```python
class Estudiante(object)

    def __init__(self, nombre_r, edad_r):
        self.nombre = nombre_r
        self.edad = edad_r

    def hola(self):
        return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad)


obj_estudiante = Estudiante("Johan", 11)
print obj_estudiante.hola()

# Mostrará Mi nombre es Johan y tengo 11
```

## Métodos especiales

- **cmp** (self, otro)

Método llamado cuando se utiliza los operadores de comparación para comprobar si tu objeto es menor, mayor o igual al objeto pasado como parámetros

- **len**(self)

Método llamado para comprobar la longitud del objeto. Lo usas, por ejemplo, cuando llamas la función **len(obj)** sobre el código. Cómo es de suponer el método debe devolver la longitud del objeto

- **init**(self, otro)

Es un constructor de nuestra clase, es decir, es un método **especial** que se ejecuta automáticamente al crear un objeto


## Condicionales IF

Las condicionales tiene la siguiente estructura. Ten en cuenta que lo que contiene los paréntesis es la comparación que debe cumplir para que la expresión se cumpla

```python
if ( a > b ):
    elementos
elif (a == b):
    elementos
else:
    elementos
``` 

## Bucle FOR

El bucle for lo puedes usar de la siguiente forma:
Recorres una cadena o lista a la cual va a tomar el elemento en cuestión con la siguiente estructura:

```python
for i in ___ :
    elementos
```

Ejemplo:
```python
for i int range(10)
    print i
```

En este caso recorrerá una lista de diez elementos, es decir, el *print i* se ejecutará 10 veces. Ahora i va a tomar cada vaor de la lista, entonces este for imprimirá los números del 0 al 9 (Recordar que en un *range* va hasta el número n-1)



## Bucle WHILE

En este caso while tiene una condición que determina hasta cuádo se ejecutará. O sea que dejarpa de ejecutarse en el momento en que la condición deje de ser cierta. La estructura de un while en la siguiente

```python
while (condicion)
    elementos
```

Por ejemplo

```python
x = 0
while x < 10:
    print x
    x += 1
``` 

En el ejemplo anterior, el programa preguntará si es menor que diez. Dado que es menor imprimirá el valor de x y luego sumará una unidad a x. Luego x es 1 y como sigue siendo menor a diez seguirá ejecutando y así sicesivamente hasta que x llegue a ser mayor o igual a 10