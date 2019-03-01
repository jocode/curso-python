# Estructuras de Datos

## Listas

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
```

> Los strings son un tipo de lista, porque son una secuencia de caracteres


## Operaciones con Listas

* Las listas soportan los operadores + y *
* Las listas al igual que los strings pueden estraerse ciertos valores (rebanadas)

Podemos sumar elementos a una lista
```python
lista_a = [2,3,4,5]
lista_b = [0,1]
lista_c = lista_b + lista_a #Agrega nuevos elementos a la lista

lista_d = ['a']
lista_e = lista_d * 5
print(lista_e) # Mostrará 5 veces 'a'
```

Para eliminar un elemento a la lista usando el keyword **del**
```python
utiles = ['cuaderno', 'lapiz', 'borrador']
del utiles[2] # Elimina borrador

lista_letter = list('casa')
print(lista_letter) # Mostrará la lista de caracteres
```


ASCII ART, son formas de dibujar por medio de letras y símbolos, gráficos en la terminal

> En python las constantes se declaran en mayuscular

*El juego del ahorcado se puede encontrar en este archivo* [ahorcado.py](ahorcado.py)


## Implementar búsqueda binaria en python

El algoritmo de lista binaria es utilizado cuando necesita buscar un elemento en una gran cantidad de datos, la búsqueda binaria es una de las mejores maneras y de las formas más poderoras para encontrar elementos en listas ordenadas (Funciona en listas ordenadas de menor a mayor)

[Busqueda binaria](binary_search.py)


## Diccionarios en pyhton

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

Los diccionarios son sirven para hacer un mapeo de objetos. Se utiliza la sintaxis de llave para crear un diccionario

### Iteración en diccionarios

* Al iterar un diccionario de manera predeterminada, se obtendrán las llaves
* Es posible también iterar a través de los valores
* También se permite obtener las llaves y los valores al mismo tiempo

```python
diccionario = {datos..}
for llave in diccionario:
    ...

for llave in diccionario.keys():
    ...

for valor in diccionario.values():
    ...

for llave, valor in duccionario.ietritems():
    ...
```

Para acceder a un elemento de un diccionario, debemos pasarle la clave (Llave) como índice

Ejemplo de diccionario
```python
calificaciones = {}
calificaciones['algebra'] = 10
calificaciones['calculo'] = 8
calificaciones['circuitos'] = 9
calificaciones['fisica'] = 10

promedio = 0
for nota in calificaciones.values():
    promedio += nota

promedio = promedio / len(calificaciones.values())

print('Su promedio es de {}'.format(promedio))
```

## Encriptar mensajes usando diccionarios

La criptografía se usa desde hace miles de años. Julio César es uno a los que se les atribuye una de las formas mas famosas de criptografía, en el cual modificaba el orden de las letras.

La encriptación se hacen con sofisticadas fórmulas matemáticas


Para este ejemplo [criptografia.py](criptografia.py) se ha utilizado un diccionario para darle valor a los caracteres, y de esta manera tomar cada uno y asignarle el valor para que no pueda ser legible. Las funciones cypher crifra el mensaje accediendo al key del diccionario y asignandole el nuevo valor al mensaje cifrado. En el caso de decifrado, hacemos lo contrario. Iteramos sobre todo el diccionario para encontrar el valor y si es el mismo, le damos la llave para decifrar el mensaje.

## Tuplas en python

* Las tuplas con una secuencia de valores indexados por enteros (integers)
* Similar a las lisas con la gran diferencua de que son __inmutables__
* Las tuplas se crean separando los valores con comas
    - Es práctica común encerrar los valores con paréntesis
* Se pueden utilizar para devolver más de un valor en una función o crear estructuras de datos ligeras
* Al igual que los strings si se quier modificar una tupla es necesario crear una nueva

```python
mi_tupla_ = 1 , 2 , 3 , 4
mi_tupla_ =  (1 ,2 ,3 ,4)
```

Encontrar el primer caracter que no se repita en un string


## Uso de sets en python

Los conjuntos (sets) son similares a las listas, y no permiten elementos repetidos.

Los sets, funcionan igual que la teoría de conjuntos en matemáticas

Las keyword utilizados son:
- **union** Une los valores de los dos conjuntos
- **intersection** Muestra sólo los elementos que se repiten en los dos conjuntos
- **difference** Muestra los elementos que no son están definido en alguno de los elementos, que no se repiten

```python
s = set([1,2,3])
t = set([3,4,5])

s.union(t) # Une los elementos de ambos conjuntos
s.intersection(t) #Nos regresa el único valor en la intersección de los conjuntos
s.diference(t) # Muestra los elementos de s, que no están en t

1 in s #True
1 in t #False
1 not in s #False
```

Es mucho más eficiente hacer operaciones con conjuntos, que con listas


## List comprehensions y Dictionary comprehensions

* Python permite crear e inicializar listas y diccionarios con una sintaxis más natural
* Convierte una secuencia en otra

Los que hace **list comprehension** es convertir una lista existente en una nueva lista

*Syntactic Sugar*
```python
pares = [num for in range(100) if num%2 == 0]
nones = [x for in range(100) if x%2 != 0]
cuadrados = { x: x**2 for x in range(100) }
```

Los que nos permite esto, es hacer más sencillo de leer el código ahorrandonos líneas de código

Por ejemplo, al utilizar dictionary comprehensions
```python
cuadrados = {}
for num in range(1,11):
    cuadrados[num] = num**1

# Sugar syntactic for this
squares = { num: num**2 for num in range(1, 11)  }
```