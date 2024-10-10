# ENVIO DE CORREO CON UN HTML CON ESTILOS EN LÍNEA

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
import string
from dotenv import load_dotenv

load_dotenv()

remitente = os.getenv('USER')
destinatario = 'pedro2076rr@gmail.com'
asunto = 'Bienvenida'

msg = MIMEMultipart()
msg['Subject'] = asunto
msg['From'] = remitente
msg['To'] = destinatario

def envioCorreo(nombre, codigo, link):
    try:
        with open('mx/com/ppware/templates/welcome.html', 'r', encoding='utf-8') as archivo:
            html_template = archivo.read()
        
        # Interpola las variables en el HTML
        html_format = html_template.format(nombre = nombre, codigo = codigo, link = link)
        
        #adjuntar contenido html
        msg.attach(MIMEText(html_format, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, os.getenv('PASSWORD'))

        server.sendmail(remitente, 
                        destinatario,
                        msg.as_string())
        server.quit()
    except:
        print("no se pudo enviar el correo desde el back-end")
        
envioCorreo("pedro", "PASHJ1", "https://open.spotify.com")
