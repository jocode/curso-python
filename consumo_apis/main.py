import requests

if __name__ == '__main__':
	url = 'https://www.google.com.co/'
	response = requests.get(url)

	if response.status_code == 200:
		content = response.content
		# wb = Escritura binaria
		file = open('google.html', 'wb')
		file.write(content)
		file.close()