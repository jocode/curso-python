import requests
import json

# Para archivos pesados usando stream
if __name__ == '__main__':
	url = 'http://i.imgur.com/n9z3sLg.jpg'

	# Realiza la peticion sin descargar el contenido
	response = requests.get(url, stream=True)
	with open('imagen.jpg', 'wb') as file:

		for chunk in response.iter_content(): # Toma el contenido y lo descarga poco a poco
			file.write(chunk)

	response.close()