import requests 
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/get'
	args = {'nombre':'Johan', 'curso':'Python', 'nivel':'intermedio'}

	response = requests.get(url, params=args)
	print(response.url)

	if response.status_code == 200:
		# Convierte el archivo json en diccionario
		"""
		response_json = response.json()
		origin = response_json['origin']
		print(origin)
		""" 
		response_json = json.loads(response.text)
		origin = response_json['origin']
		print(origin)
		