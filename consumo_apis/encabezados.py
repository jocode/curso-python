# -*- coding: utf-8 -*-
import requests
import json

"""
Tanto el cliente como el servidor están obligados
a enviar encabezados
Los encabezados permiten tener una comunicación correcta
OAuth
"""

if __name__ == '__main__': 
	url = 'http://httpbin.org/post'
	payload = {'nombre':'Johan', 'curso':'Python', 'nivel':'Intermedio'}
	headers = {'Content-Type': 'application/json', 'access-token':'12345'}

	response = requests.post(url, data=json.dumps(payload), headers=headers)

	print(response.url)

	if response.status_code == 200:
		#print(response.content)
		headers_response = response.headers # Dic
		server = headers_response['Server']
		print(headers_response)