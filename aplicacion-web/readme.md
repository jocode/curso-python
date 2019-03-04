# Servidor web

Vamos a utilizar Google App Engine para el desarrollo de la aplicación web

1. Descargamos el SDK de google en [Download and Install the SDK for App Engine](https://cloud.google.com/appengine/downloads)
2. Extraemos los archivos
3. Ejecutamos el script `./install.sh`

https://cloud.google.com/sdk/docs/quickstarts

Luego creamos los archivos que App Engine necesita para ejecutar nuestro programa

* app.yaml
* appengine_config.py

Luego de eso creamos el ambiente virtual en la carpeta 

* `virtualenv venv`

* `source venv/bin/activate`

* Creamos una carpeta llamada __lib__, donde colocaremos todas las dependencias que usará el proyecto

* `pip install -r requirements.txt -t lib` Ejecutamos este comando para instalar las librerías colocadas en el requerimiento el **-t** indica el destino que es **lib**


**Por último configiramos [app.yaml](app.yaml)**

Y ejecutamos el comando

* `dev_appserver.py .`  El **.** le indica que el archivo app.yaml se encuentra en el mismo directorio

Luego que lo ejecutemos nos pedirá instalar algunas extensiones

Al instalarlas, ingresamos a [Google Cloud Console](https://console.cloud.google.com) accedemos a la cuenta y creamos un proyecto (Tenemos en cuenta el id del proyecto)

* Seleccionamos en el menú la opción App Engine y escogemos el lenguaje

* __Traemos las credenciales de google a la computadora__

* `gcloud auth login` Nos abrirá una pestaña en eñ mavegador y nos autenticamos

* `gcloud app deploy --project id_code` Le damos enter y empezamos a hacer deploy


## Templates con Jinja2

Debemos importar una función de flask llamada **render_template**, por defecto Flask busca los archivos en un directorio llamado **templates**

```python
from flask import Flask, render_template, request
from ContactModel import ContactModel
```

El ContactModel es un modelo que creamos usando la librería **ndb** de AppEngine para tratar con base de datos

- **IMPORTANTE**

Luego de haber instado app Engine y ejecutarlo para que se encenciera el servidor, la información de la aplicación no era visible en el sitio web, no se mostraba nada de los que se tenía. El problema era que por defecto App Engine requiere el módulo SSL, de modo que en el archivo app.yaml, se debe especificar la librería requerida:

```
libraries:
- name: ssl
  version: latest
``` 

*Para más información ver*
* https://cloud.google.com/appengine/docs/standard/python/sockets/ssl_support
* https://stackoverflow.com/questions/5128845/importerror-no-module-named-ssl#31643606


## Mostrar los datos de la base de datos

Para leer la base de datos utilizamos el método **query()** de la clase *ContactModel*, de la siguiente manera:

```python
@app.route(r'/', methods=['GET'])
def contact_book():

    contacts = ContactModel.query().fetch()

    # Luego le pasamos los contactos como parámetro al render_template
    return render_template('contacts_book.html', contacts=contacts)
```

Para ver más sobre el proyecto, ver el archivo [main.py](main.py)

* Finalmente se hace deploy al servidor

`gcloud app deploy --project project-id`


Nos pederirá si queremos hacer deploy, le damos que sí y los archivos se subirán al servidor remoto