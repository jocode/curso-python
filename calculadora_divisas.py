# -*- coding: utf-8 -*-

# Declaración de funciones
def run():
	print('CALCULADORA')
	print('convierte pesos mexicanos a colombianos')
	ammount = float(raw_input('ingresar el numero de pesos mexicanos: '))
	result = foreign_exchange_calculator(ammount)

	print ('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))


def foreign_exchange_calculator(ammount):
	mex_to_col_rate = 145.97
	return mex_to_col_rate*ammount

if __name__ == '__main__':
	run() # Se llama la función run() como principal


 