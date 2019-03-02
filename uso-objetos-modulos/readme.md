# Uso d objetos y módulos

## Manejo de errores

* Cuando se avienta y (**throw**) un error, si el error no se "atrapa", entonces el programa se detiene
* Hay veces que queremos evitar este comportamiento porque sabemos como arreglar el error
* Para manejar el error se utilizan los keywords **try**/**except**

```python
mi_string = 'Mi string'

try:
    int(mi_string)
except ValueError:
    # Maneja el error
finally:
# Se ejecuta pase lo que pase
```

*Jerarquía de errores en python*

- **try/except/else/finally** 
* La cláusula **else** se ejecuta si no han ocurrido excepciones y antes de la cláusula **finally**


## Errores personalidos

Cada vez que sea probable que suceda un error, encapsulelo y trate de manejar el error para hacer al usuario más feliz y que no se esté cerrando la aplicación. ¡Es importante para hacer software robustos!

Para este caso se ha hecho un script que nos diga la población en millones en los paises latinoamericanos [errores.py](errores.py)


## Manejo de archivos

* Python puede leer y escribir archivos con la función **open**
* La función **open** regresa un objeto archivo (file)
* Los archivos pueden er de texto o binarios
* Se tiene que especificar el modo en que se maneja el archivo
    - 'r' = read
    - 'w' = write
    - 'a' = append
    - 'r+' = read and write
* Se debe cerrar el archivo con el método **close**
* La mejor manera de manejar archivos es con el keyword **with** (Manejador de contexto)


### Lectura de archivos

El objeto archivo tiene dos métodos para leerlo
- **read**
- **readlines**

```python
with open('file.txt', 'r') as f:
    for line in f:
        print(line)
```

### Escrituta de archivos

Para escribir a un archivo, se utiliza el método **write**

```python
with open('file.txt', 'w') as f:
    for i in range(5)
        f.write(i)
```

Contar una palabra al leer un archivo
```python
def run():
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra {} en el archivo'.format(counter))

if __name__ == '__main__':
    run()
```


## Programación Orientada a Objetos

### Clases y Objetos

* Permite definir tipos propios
* Permite manejar datos y lógica en un sólo contenedor
* Las clases con como fábricas (moldes) para crear objetos

- **Atributos**

* Los objetos tienen atributos que se pueden definir al momento de inicializar un nuevo objeto o directamente en la *instancia*
* Las clases pueden tener variables de clase, variables de instancia y variables locales
* Aunque python no tiene el concepto de variable privadas integrado al lenguaje, es práctica común definirlas con un *guión bajo*
* __isinstance__ y __hasattr__


- **Métodos**

* Los métodos son como funciones que tienen sentido únicamente en el contexto de una clase.
* Al igual que las variables, los métodos privados se definen con un guión bajo
* La **encapsulación** es un concepto clave en la programación orientada a objetos
    * La forma práctica de aplicar este principio es declarar todas las variables y métodos como privados, a menos de que sea necesario exponerlos a otras clases
* Un método clave que casi todas las clases deben tener es **__init__**
* Otro es **__str__**
* Existen varios tipos de métodos estáticos, de clase, de instancia, getters y setter.


### Modelar un objeto en Python

En python **__** dos guiones bajos se llaman "thunder", de modo que el **__init__** se le conoce como "el método thunder init"

El ejemplo de definición e instancia de clase se puede ver eb [lamp.py](lamp.py)


## Decoradores

Un decorador es una función que recibe como parámetro una función y regresa otra función

* Un decorador es una función que recibe como parámetro a otra función y modifica su comportamiento
* Un decorador se aplica a una función o método con el símbolo **@**
* Súper útil para definir si una función debe ejecutarse o no
    - Por ejemplo, en servidores web, existen ciertas funciones que nada más deben ejecutarse si un usuario se encuentra autenticado

Si usas Frameworks como Flask o Django se encontrarás con muchos de ellos. Son simplemento una forma de sintax sugar.


## Paquetes y módulos

* Un módulo permite agrupar funcionalidad común en un sólo archivo
* Cuando varios módulos agrupan funcionalidades comunes, se pueden agrupar a su vez, en paquetes
* Python reconoce que un directorio es un paquete porque contiene llamado un archivo llamado **__init__.py**

> Cada script que generamos en python se conoce como módulo



## Entorno virtual en python

Muchos de los problemas que se te pueden ocurrir, seguramente ya alguien los ha programado en forma de librería o paquete.
Cada vez que un programador quiere compartir una funcionalidad, sube el archivo al PyPi (python package index)

### Paquetes de tercetos

* PyPi (python package index) es un repositorio de paquetes de terceros que se pueden utilizar en proyectos en python
* Para instalar un paquete, es necesario utilizar la herramienta **pip**.
* La forma de instalar un paquete es ejecutando el comando `pip install nombre-paqueta`
* También se puede agrupar la instalación de varios paquetes a la vez con el archivo **requierements.txt**


### Ambientes virtuales

* Es una buena práctica crear un ambiente virtual por cada proyecto de Python en el que se trabaje
* Esto evita conflictos de paquetes en el intérprete principal
* `pip install virtualenv`
* `virtualenv venv`
* `source venv/bin/activate`
* `deactivate`


**¿Cómo instalar pip?**

Podemos buscar `pip instalation`, esto nos arrojará resultados, y podemos instalar la versión que nosotros deseemos

El link para buscar el archivo es https://bootstrap.pypa.io/get-pip.py

Ese archivo lo descargamos y lo ejecutamos en la terminal, escribiendo el comando

* `python get-pip.py`

Si se da el caso en que en linux genere error por permisos, se debe indicar el parámetro **--user**

`python get-pip.py --user`

- **¿Cómo sabemos si tenemos instalado pip?**

Sólo debemos ejecutar el comando `which pip`

Luego que tengamos instalado pip, podemos instalar cualquier tipo de paquete

- **instalar ambientes virtuales**
`pip install virtualenv --user`

* `pwd` muestra la ruta donde se encuentra el directorio

* `virtualenv venv` Generamos el ambiente virtual

* `source venv/bin/activate` Se activa el ambiente virtual

* `pip freeze` Muestra los paquetes instalados

* `pip install flask` Este paquete nos permite crear servidores

* `touch requirements.txt` Creamos el archivo requirements.txt

Luego copiamos la librería en el archivo creado, en este caso fué la de Flask
*Flask==1.0.2*

Y finalmente creamos un archivo [main.py](main.py), donde importaremos la librería de Flask y la usaremos para crear el servidor