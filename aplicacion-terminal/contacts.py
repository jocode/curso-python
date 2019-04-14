# -*- coding: utf-8 -*-
from ContactBook import ContactBook
import csv

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)

        for index, row in enumerate(reader):
            if index == 0:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])

    while True:

        command = str(raw_input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Ingresa el telefono: '))
            email = str(raw_input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

            print('Contacto guardado\n')

        elif command == 'ac':
            name = str(raw_input('Escribe el nombre del contacto: '))
            if not contact_book.search(name):
                break
            new_name = str(raw_input('\nEscribe el nuevo nombre: '))
            phone = str(raw_input('Escribe el nuevo telefono: '))
            email = str(raw_input('Escribe el nuevo email: '))
            contact_book.update(name, new_name, phone, email)
            print('\nContacto modificado')

        elif command == 'b':
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.delete(name)
            print('Contacto eliminado\n')

        elif command == 'l':
            contact_book.showAll()

        elif command == 's': 
            print('Salir\n')
            break
        else:
            print('Comando no encontrado')

    print('')

if __name__ == "__main__":
    run()