# Uso de strings y Ciclos

El algoritmo se lee como una secuencia de pasos de arriba hacia abajo y de izquierda a derecha.

## Recursión

La recursión es un concepto, en el cual una función puede llamarse a sí mismo dentro de ella.

La función factorial consiste en multiplicar cada uno de los númros anteriores.

* 5! = 5 * 4 * 3 * 2 * 1

```python
def factorial(n):
    if (n==0):
        return 1
    else
        return n * factorial(n-1)
```

Si no se establece un caso base, la función recursiva se ejecutará indefinidamente


## Manejo de Strings

Los string son una secuencia de caracteres, se componen de caracteres. 

Los caracteres se pueden acceder por índice, por ejemplo
```python
my_string = 'johan'
my_string[2] # Mostrará h
```

* __len()__ Devuelve el tamaño del string
- **upper()** 
- **isupper()**
- **lower()**
- **islower()**
- **find()**
- **isdigit()**
- **endswith**
- **startwith()**
- **split()**
- **join()**

Por ejemplo

`my_string.upper() # Devuelve todo en mayúscula`

* __find()__ encuentra la primera coincidencia del string
`my_string.find('F') # Devolverá la primera posición en la que se encuentra el caracter`


## Separar cadenas de texto

Se puede obtener una substring utilizando la notación de slices (rebanadas)

```python
my_string = "Hola mundo"
my_string[5:9] # Mostrará mund (es último -1)

my_string[::-1] # Invierte la los caracteres
# my_string[inicio:fin:saltos]
```

## Comparación de Strings y Unicode

Los strings son inmutables. Una vez que se crea no puede modificarse

```python
s = 'Hola'
r = 'l' + s[1:] # desde [1:] se entiende que es el final
r # Obtendrá lola
```

Los operadores dependen del conexto. En los string, es igual a otro si contiene los mismos caracteres.

* Una string es menor que otra si sus caracteres se encuentran antes en un orden **lexicográfico**

```python
'johan'=='camilo' # false
'johan'>'camilo' # false
```

## ASCII vs Unicode

* Ambos son codificadores de caracteres
* ASCII (American standard code for information interchange) `reconoce solo caracteres en ingles (128 caracteres)`
* UNICODE incluye la mayoría de los alfabetos del mundo


Python 2, asume que los string están en ASCII
Python 3, asume que los string estás en UNICODE

Para decirle a python que los caracteres son Unicode podemos usar `u'niño'`


## Ciclos

* Las iteraciones permiten realizar la mimsa secuencia de pasos varias veces
* También permiten recorrer una secuencia (como in string)
* Es una de las herramientas clave de cualquier programador

```python
range(5) # Genera una secuencia de números desde el 0 hasta 5-1 (El último número no se incluye)

""" Rango con pasos """"
range(desde, hasta, con_paso)
range(5, 40, 5) # Imprimirá los números comprendidos entre 5 y 40, avanzando de 5 en 5 (Recuerde que el último valor no lo toma)
```


* Iteración con ciclo for

```python
for i in range(5):
    print(i)
```


### For loop

* Se puede utilizar para recorrer strings
* Se necesita el keyword **in**
* Si se requiere salir antes de una iteración se utiliza el keyworkd **break**
* Si se requiere pasar a la siguiente iteración se utiliza el keyword **continue**

```python
for i in range(30):
    if (i%3 != 0):
        continue
    else:
        print(i**2)

## Ciclo usando break
for i in range(30):
    if (i%3==0):
        print(i)
    elif (i==22):
        break
```


* Iterar sobre un string, sería un ciclo "foreach" como se conoce en otros lenguajes
```python
miString = 'Ferrocarril Parado'

for letra in miString:
    print(letra)
```


### loop while

* Es similar a un for, pero en lugar de recorrer una secuencia, se ejecuta hasta que una condición se convierta en falsa.
* Se debe tener mucho cuidado de no caer en un **infinite loop**

```python
i = 0
while i > 0:
    print(i)
    i += 1
```

> Si por alguna razón tiene un ciclo indefinido, hay una forma de detenerlo es usar el comando **`ctrl + c`**


**Importante** Cuando nosotros colocamos un nombre al archivo que tenga un *mismo* nombre que el módulo nos generará un error porque no encontrará las funciones en el módulo (Que sería nuestro script). Por eso es bueno nombrar los archivos diferentes a los que vienen el los módulos

- **Palíndromo** Es una palabra que se lee igual al derecho y al revés