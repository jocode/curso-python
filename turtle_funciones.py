# -*- coding: utf-8 -*-
import turtle

def main():
	window = turtle.Screen()
	tortuga = turtle.Turtle()

	make_square(tortuga)
	turtle.mainloop()

def make_square(turtle):
	lenght = int(raw_input('Digite el largo del lado: '))
	
	for i in range(4):
		make_line_and_turn(turtle, lenght)

def make_line_and_turn(turtle, lenght):
	turtle.forward(lenght)
	turtle.left(90)

# Le indicamos a python que ejecute el método de entrada
if __name__ == '__main__':
	main()