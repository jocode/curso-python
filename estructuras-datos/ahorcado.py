# -*- coding: utf-8 -*-
import random

# Las constantes se declaran es mayúsculas
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ========''', '''

''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'computador',
    'telefono',
    'equipo',
    'tablet',
    'audifono'
]

def run():
    word = random_word()
    # Mostramos las rayas de cada caracter
    hidden_word = ['-'] * len(word) 
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(raw_input('Escoge una letra: '))

def random_word():
    indice = random.randint(0, len(WORDS)-1 )
    return WORDS[indice]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * ---- * --- * ---- * --- * ----')

if __name__ == "__main__":
    print('\nB I E N V E N I D O S  A  A H O R C A D O S')
    run()