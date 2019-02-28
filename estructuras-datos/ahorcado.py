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

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries +=1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('¡Ouhhs Perdiste! La palabra correcta era {}'.format(word))
                break

        else:
            # Reemplazamos la  letra en la palabra oculta
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            
            letter_indexes = []

        # Si no queda ningun simbolo -, significa que ganaste
        try:
            hidden_word.index('-')
        except ValueError:
            display_board(hidden_word, tries)
            print('\n¡Felicidades, ganaste! Has encontrado la palabra :)')
            break

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