from re import search
import smtplib

def enviar_correo(asunto, mensaje, correo):

    mensaje = 'Subject: {}\n\n{}'.format(asunto, mensaje)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('originnot.reply@gmail.com', 'origin123456')


    server.sendmail('originnot.reply@gmail.com', correo, mensaje)

    server.quit()