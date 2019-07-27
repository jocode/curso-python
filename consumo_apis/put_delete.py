import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/delete'
	payload = {'nombre':'Johan', 'curso':'Python', 'nivel':'intermedio'}
	headers = {'Content-Type': 'application/json', 'access-token':'1234'}

	response = requests.delete(url, data=json.dumps(payload), headers=headers)
	print(response.url)

	if response.status_code == 200:
		headers_response = response.headers # Dic
		server = headers_response['Server']
		content = response.content
		print(server)


	"""
	GET => Obtener
	POST => Crear
	PUT => Actualizar
	DELETE => Eliminar
	"""