# -*- coding: utf-8 -*-
import random

def run():
    number_found = False
    random_number = random.randint(0, 20)
    print('Vamos! Adivina el número.\n')

    while not number_found: # El not, cambia el valor del booleano
        number = int(raw_input("Intenta un número: "))

        if (number == random_number):
            print('Felicidades, encontraste el número!')
            number_found = True
        elif number>random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == '__main__':
    run()