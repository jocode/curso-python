# -*- coding: utf-8 -*-

""" Los números primos son aquellos que se pueden dividir por 1 o por ellos mismos """

def run():
    number = int(raw_input('Escribe un número: '))
    result = is_prime(number)
    
    if result is True:
        print('Tu número '+str(number)+' es primo')
    else:
        print('Tu número '+str(number)+' NO es primo')


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number%2==0:
        return False
    else:
        for i in range (3, number):
            if number % i == 0:
                return False
    return True

if __name__ == "__main__":
    run()