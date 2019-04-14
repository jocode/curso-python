# -*- coding: utf-8 -*-
import smtplib

message = 'Hola, un mensaje desde python!'
subject = 'Prueba de correo'

message = 'Subject: {}\n\n{}'.format(subject, message)

# Definimos el objeto SMTP, recibe el servidor de correo y el puerto a utilizar
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# Se puede colocar la 'contraseña' como variable de entorno
server.login('emailfrom@email.com', 'password')

from_addr = "emailfrom@email.com";
to_addrs = "emaildestine@email.com"
server.sendmail(from_addr, to_addrs, message)

# Indicamos al servidor que cerramos la sesión
server.quit()

print("Correo enviado exitosamente!")