# -*- coding: utf-8 -*-
import threading
import time
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

def consultar(id_persona):
	logging.info("Consultando para el id "+str(id_persona))
	time.sleep(2)

def guardar(id_persona, data): 
	logging.info("Guardando para el id "+str(id_persona)) 
	time.sleep(5)

tiempo_ini = datetime.datetime.now()

thread1 = threading.Thread(name="hilo_1", target=consultar, args=(1, ))
thread2 = threading.Thread(name="hilo_2", target=guardar, args=(1, "¡Bienvenido a los Threadings!"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido "+str(tiempo_ini.second - tiempo_fin.second))