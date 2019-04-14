# -*- coding: utf-8 -*-

def first_not_repeating_char(char_secuence):
    seen_letter = {}

    for index, letter in enumerate(char_secuence):
        if letter not in seen_letter:
            seen_letter[letter] = (index, 1)
        else:
            seen_letter[letter] = (seen_letter[letter][0], seen_letter[letter][1] + 1)

    final_letters = []
    for key, value in seen_letter.iteritems():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'

if __name__ == '__main__':

    char_secuence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_secuence)

    if (result == '_'):
        print('Todos los caracteres de repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))