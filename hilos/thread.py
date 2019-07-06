# -*- coding: utf-8 -*-

"""
Hilos:
Es un  concepto de la programación o de la informática.
Un Hilos es una unidad de procesamiento que se puede ejecutar.
Los hilos en python se puede crear con una librería que nos ofrece el lenguaje
Se utilizan cuando queremos realizar varias tareas a la vez.

Los hilos y los procesos tienen diferencias
En los hilos la memoria es compartida.
En un programa siempre hay un hilo, que se le denomina Hilo principal
"""

import threading 
import time

class MiHilo(threading.Thread):

	#
	def run(self):
		print("{} inicio".format(self.getName()))
		time.sleep(1)
		print("{} terminado".format(self.getName()))


if __name__ == "__main__":
	for x in range(4): 
		hilo = MiHilo(name="Thread-{}".format(x+1))
		hilo.start()
		time.sleep(.5)
