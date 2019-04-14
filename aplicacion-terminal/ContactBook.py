# -*- coding: utf-8 -*-
from Contact import Contact
import csv

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        # Cuando añadimos, guardamos la lista
        self._save()

    def showAll(self):
        for contact in self._contacts:
            self._printContact(contact)

    def delete(self, name):
        for index, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[index]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._printContact(contact)
                return True
        else:
            self._notFound();
            return False

    def update(self, name, new_name, phone, email):
       for index, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self._contacts[index].name  = new_name
                self._contacts[index].phone  = phone
                self._contacts[index].email  = email
                self._save()
                break

    def _save(self):
        # csv: comma separated values
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow( 
                    (
                        contact.name,
                        contact.phone,
                        contact.email
                    )
                )

    def _printContact(self, contact):
        print('---*---*---*---*---*---*---*---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Correo: {}'.format(contact.email))
        print('---*---*---*---*---*---*---*---')

    def _notFound(self):
        print('********')
        print('¡No encontrado!')
        print('********')