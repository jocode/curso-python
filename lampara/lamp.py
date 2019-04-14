# -*- coding: utf-8 -*-

class Lamp:

    _LAMPS = ['''

           . 
     .     |     .
      \    |    /
       . .---. .        
    --- (     ) ---  
         \ _ /
         _|_|_
        |_____|

    ''',
    '''

         .---.         
        (     )  
         \ _ /
         _|_|_
        |_____|
        
    ''']

    # self es la instancia de la clase, siempre toda clase en python la debe llevar y __init__ es el constructor
    def __init__(self, is_turn_on=False):
        self._is_turned_on = is_turn_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()
    
    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

