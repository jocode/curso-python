# -*- coding: utf-8 -*-
import requests 

"""
Con el método post creamos un recurso en el servidor
"""

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = {'nombre':'Johan', 'curso':'Python', 'nivel':'intermedio'}

	# Si colocamos data=payload, los datos se enviarán en el atributo form y no en data
	# data = json.dumps(payload) Serializa los datos y los envía en data
	response = requests.post(url, json=payload )

	# json => post se encarga de searizarlos
	# data => entonces nosotros debemos serializarlo
	print(response.url)

	if response.status_code == 200:
		content = response.content
		print(content)