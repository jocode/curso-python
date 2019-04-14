""" Strings """
print("Hola mundo")
print('Hola mundo vagabungo')
print('''Hello world''')
print("""Hello world vagabundo""")

# Con + podemos unir (Contatenar) strings
uno = "Bye "
name = "Johan Camilo"
print(type(name))

print(uno + name)

""" Numeros (int) """
print(20)
print(30+12)
print(type(11))


""" Numeros (float) """
print(12.3)
print(type(5.5))
print(6+8.6)

""" Booleanos (Verdadero o Falso) """
print(True)
print(type(False))


""" Listas (list) """
lista = list()
lista_a = [1,4,5,4,6]
lista_b = ["Buenas", "Chao", True, 12]


""" Tuplas (Los datos no cambian) """
tupla = tuple()
tupla_a = (1,5,6,3,4) # Son inmutables
tupla_b = ("Chao", "Hola", 2, True)

""" Diccionarios (Agrupa datos por forma clave => valor) """
dicc = dict()
dict_a = {
    "name": "Johan Mosquera",
    "nickname": "jocode",
    "age": 11
    }