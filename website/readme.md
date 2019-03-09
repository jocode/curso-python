# Sitio web con Python

Creamos el archivos que va a arrancar la aplicación llamado `index.py`

Vamos a utilizar **Flask** que es un framework sencillo de python para crear aplicaciones web

Para instalar flask podemos instarlo usando *pip*

* `pip install flask` En python 2

* `pip3 install flask` En python 3


Para desinstalar un módulo usamos el comando

* `pip uninstall flask`

Esto nos instalará flask en todo el computador, donde lo podemos usar en cualquier proyecto

Luego usamos un decorador, que nos permitirá manejar las rutas en python


En el archivo [index.py](index.py), importamos Flask y usamos los decoradores para crear las rutas de la aplicación 


Si queremos evitar reiniciar el sevidor cada vez que se haga un cambio, podemos usar la opción **debug=True** en el punto de entrada del sitio web

```python
if __name__ == "__main__":
    app.run(debug=True)
```

En este ejemplo utilizamos Jinja2 como motor de templates y bootstrap para la maquetación de nuestro sitio

*Página para gradientes* [uigradients](https://uigradients.com/)

## Despliegue

Para el despliegue vamos a utilizar *Heroku*, que nos provee un servicio gratuito para hacer pruebas

Primero preparamos el entorno virtual, esto nos permitirá separar nuestro proyecto de otro proyecto de python con sus propias dependencias

Instalamos el modulo de entorno virtual, luego ejcutamos el comando

* `python -m venv venv`

Luego nos dirigimos a la carpeta *venv/bin/* e instalamos flask

* `pip3 install flask` 

De esta manera los instala sólo en el entorno virtual

Podemos ver el entorno virtual funcionando al ejecutar

* `python3 ../../src/index.py`

De esta manera nos ejecutará el script desde el entorno virtual


Ahora para hacer el despliegue, podemos descargar **Heroku CLI**, que es una herramienta de consola para subir las aplicaciones

Para el despliegue debemos crear 3 archivos

* **requirements.txt**  Especifica las dependencias que necesita el proyecto
* **runtime.txt** Indica la versión de python con la cual se va a ejecutar
* **Procfile** Indicamos el archivo que debe ejecutarse con Heroku

Se necesita **Gunicorn** es un complemento que Heroku necesita para ejecutar nuestro servidor HTTP

Este comando debe ejecutarse desde nuestro entorno virtual `venv/bin/`
* `pip install gunicorn`

Este lo utilizamos en el archivo *Procfile*

* `pip3 freeze` Muestra las dependencias del proyecto

* `pip3 freeze > ../../src/requirements.txt` Copia las dependencias en el archivo requirements


Creamos el repositorio de git en la carpeta **src**

* `git init`
* `git add .`
* `git status`
* `git commit -m "Primeros archivos"`

**Creamos una aplicacion de Heroku**

* `heroku create first-website-python` Nos crea una aplicacion con el nombre *first-website-python*, si no le especificamos nada, Heroku le dará un nombre por nosotros

* `heroku login` Nos autenticamos desde la línea de comandos 

Enlazamos el proyecto

* `heroku git:remote first-website-python` Enlazamos el proyecto

* `git push heroku master` Enviamos los archivos al repositorio remoto