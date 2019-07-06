# -*- coding: utf-8 -*-
# Importamos la librería threading
import threading
import time

def hola_mundo(nombre):
	print("Hola mundo " + nombre)
	time.sleep(5)

if __name__ == '__main__':
	# Generamos un nuevo objeto, indicando que funcion se ejecutará en segundo plano
	thread = threading.Thread(target=hola_mundo, args=("Johan",))
	thread.start()
	#thread.join() # Indica al otro hilo que espere para que se ejecute el codigo

	print("Hola Mundo desde el hilo principal")