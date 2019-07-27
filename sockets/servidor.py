# -*- coding: utf-8 -*-
import socket

mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000 ) )
mi_socket.listen(5) # Numero de conexiones

while True:
	conexion, addr = mi_socket.accept()
	print("Nueva conexión establecida")
	print(addr)

	peticion = conexion.recv(1024)
	print(peticion)
	# Enviamos un mensaje
	""" Se pueden enviar, texto, archivos (imágenes, mp3)"""
	conexion.send("Hola, te saludo desde el servidor")
	conexion.close()

