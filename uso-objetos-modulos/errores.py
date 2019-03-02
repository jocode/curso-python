# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(raw_input('\nEscribe el nombre de un país: ')).lower()
    
    try:
        print('La polación de {} son: {} millones'.format(country, countries[country]))
    except KeyError:
        print('NO tenemos el dato de la población de el pais {}'.format(country))
