# -*- coding: utf-8 -*-

def palindrome2(word):
    # Tomará el slide desde atrás hacia adelante
    reversed_word = word[::-1]
    if (reversed_word == word):
        return True
    return False

def palindrome(word):
    reversed_letter = []
    for letter in word:
        # El método insert agrega un nuevo elemento a la secuencia
        reversed_letter.insert(0, letter)

    reversed_word = ''.join(reversed_letter)

    if (reversed_word == word):
        return True
    else:
        return False

if __name__ == '__main__':
    word = str(raw_input('Escribe una palabra: '))

    if ( palindrome2(word) ):
        print('La palabra {} es un palíndromo.'.format(word))
    else:
        print('La palabra {} NO es un palíndromo.'.format(word))