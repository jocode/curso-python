# -*- coding: utf-8 -*-

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '-',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',

    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'o',
    'T': 'P',
    'U': 'h',
    'V': 'h',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',

    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B'
}

def crypher(messaje):
    words = messaje.split(' ')
    crypher_messaje = []

    for word in words:
        crypher_word = ''
        for letter in word:
            crypher_word += KEYS[letter]

        crypher_messaje.append(crypher_word)

    return ' '.join(crypher_messaje)


def decipher(messaje):
    words = messaje.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''
        for letter in word:
            for key, value in KEYS.iteritems():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)

def run():

    while True:

        command = str(raw_input('''
            --- * --- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            print('Cifrar'
            )
            messaje = str(raw_input('Escribe tu mensaje: '))
            crypher_messaje = crypher(messaje)
            print(crypher_messaje)

        elif command == 'd':
            print('Descrifrar')
            message = str(raw_input('Escribe tu mensaje cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)

        elif command == 's':
            print('Salir')
            break
        else:
            print('Comando no encontrado')

if __name__ == '__main__':
    print('M E N S A J E S     C I F R A D O S')
    run()