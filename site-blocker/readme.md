# Bloqueador de sitios

Bloquea los sitios web que visitamos a diario

* Programa que te ayudará a evitar la procrastinación
* Te ayudará a practicar en python


En cada sistema operativo hay un archivo llamado **hosts**, aquí hay un listado de sitios que usa el SO. En este archivo vamos a modificar ese archivo para que en determinadas horas bloquee sitios que evitan que nos concentremos.

Los sitios los bloquearemos redireccionandonos a otra ruta.

Para Unix (Mac y linux) la ruta es

* `/etc/hosts`

En windows seria

* `c:\\windows\system32\drivers\etc\hosts`


Para eso trajaremos con la biblioteca **datetime**

* **datetime.now()** Nos devuelve la hora actual