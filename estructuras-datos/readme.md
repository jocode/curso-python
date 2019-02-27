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