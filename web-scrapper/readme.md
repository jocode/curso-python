# Web Scrapper

## Qué es web Scrapper

Web scraping es una técnica utilizada mediante programas de software para extraer información de sitios web. Usualmente, estos programas simulan la navegación de un humano en la World Wide Web ya sea utilizando el protocolo HTTP manualmente, o incrustando un navegador en una aplicación.

El web scraping está muy relacionado con la indexación de la web, la cual indexa la información de la web utilizando un robot y es una técnica universal adoptada por la mayoría de los motores de búsqueda. Sin embargo, el web scraping se enfoca más en la transformación de datos sin estructura en la web (como el formato HTML) en datos estructurados que pueden ser almacenados y analizados en una base de datos central, en una hoja de cálculo o en alguna otra fuente de almacenamiento. Alguno de los usos del web scraping son la comparación de precios en tiendas, la monitorización de datos relacionados con el clima de cierta región, la detección de cambios en sitios webs y la integración de datos en sitios webs. También es utilizado para obtener información relevante de un sitio a través de los rich snippets.

En los últimos años el web scraping se ha convertido en una técnica muy utilizada dentro del sector del posicionamiento web gracias a su capacidad de generar grandes cantidades de datos para crear contenidos de calidad

*Referencia *[Wikipedia](https://es.wikipedia.org/wiki/Web_scraping)


En este módulo descargaremos imágenes de un sitio web utilizando un web scrapper

1. Creamos el ambiente virtual
    - Nos ubicamos en la carpeta donde lo queremos crear
    - Colocamos el comando
    `virtualenv venv`
    - Luego que lo creamos, accedemos a él y activamos el ambiente
    `source venv/bin/activate`
    - Guardamos las dependencias en el archivo *requerements.txt*, ahí definimos las versiones de las librerías que vamos a utilizar, las librerías utilizadas en este proyecto son:
        - **requests** Nos permite hacer solicitudes a internet y traer el contenido html de sitios web (Cualquier contenido que esté en internet)
        - **beatifulsoup4** Permite acceder al contenido del sitio, parseando la información consultada por la librería
    - Instalamos las dependencias
    `pip install -r requirements.txt` 
    - Comprobamos si están instaladas las librería con
    `pip freeze`

2. Luego que tenemos configurado el entorno virtual, vamos al sitio web que queremos consultar (xkcd.com/1/), y observamos la estructura y hacemos el script [web_scrapping.py](web_scrapping.py)


Con esto, podemos automatizar tareas, haciendo el trabajo manual y repetitivo en algo más práctico con este proceso.