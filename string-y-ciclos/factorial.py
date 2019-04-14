# -*- coding: utf-8 -*-

def factorial(number):
    if (number == 0):
        return 1
    
    return number * factorial(number - 1)

if __name__ == "__main__":
    print("\nCalcular el factorial")
    number = int(raw_input("Escribe un número: "))
    result = factorial(number)
    print("El resultado de " + str(number) + "! es: " + str(result))