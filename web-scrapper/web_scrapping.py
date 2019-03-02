# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib # Guarda las imágenes que estamos trayecto

def run():
    for i in range(1, 6):
        # Hacemos la petición del sitio web
        response = requests.get('https://xkcd.com/{}'.format(i))
        # Parseamos el documento
        soup = BeautifulSoup(response.content, 'html')

        # Accedemos a la etiqueta img y obtenemos la url
        image_container = soup.find(id='comic')
        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]

        print('Descargando la imagen {}'.format(image_name))

        # Guadamos la imagen
        urllib.urlretrieve('https:{}'.format(image_url), image_name)

        # Las imágenes se van a guardar en elmismo directorio donde ejecutamos el programa

if __name__ == "__main__":
    run()