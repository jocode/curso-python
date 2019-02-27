# -*- coding: utf-8 -*-

def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)

    return sum_of_temps/len(temps)

if __name__ == "__main__":
    print('\nVamos a calcular la temperatura promedio')
    temps = [21, 24, 22, 23, 24, 25, 21]

    promedio = round(average_temps(temps), 2)
    print('La temperatura promedio es: {}'.format(promedio))