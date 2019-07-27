# -*- coding: utf-8 -*-
import socket

mi_socket = socket.socket()
mi_socket.connect( ('localhost',8000) )

mi_socket.send('Hola, desde el cliente')
# 1024 hace referecia al buffer (1024 bytes)
respuesta = mi_socket.recv(1024)

print(respuesta)
mi_socket.close()