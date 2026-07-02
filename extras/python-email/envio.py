'''
App: envío de email, basándonos en una cuenta de cualqueir proovedor externo compatible
con el protocolo SMTP (protocolo de email de salida en servidores de email),
Un servidor de email externo puede ser:
    - Gmail     - Proton    - Hotmail/Outlook/MSN   - Yahoo     - ...

** Este protocolo está, a día de hoy, sólo parcialmente securizado **

Los login de email, normalmente, tienen la siguiente estructura:
    - usuario: remitente
    - password: ??
'''
# IMPORTS ---------------------------------------
import smtplib # https://docs.python.org/3/library/smtplib.html
from email.message import EmailMessage # https://docs.python.org/3/library/email.message.html

# FUNCTIONS -------------------------------------
def enviar_email(remitente, destinatario, asunto, cuerpo, password):
    # Creación de un objeto: es una caja para contener toda la información recibida
    mensaje = EmailMessage() # creo una caja de tipo Email

    # cargamos cada cosa en su lugar, actuando como una especie de diccionario
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.set_content(cuerpo) # es un setter, obligamos a que tenga un contenido determinado por nosotros

    # Carga del email (cliente) externo

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smpt:
        # smtplib.SMTP_SSL("smtp.gmail.com", 465).login(remitente, password)
        smpt.login(remitente, password) # user: remitente
        smpt.send_message(mensaje) # se envía TOÍTO

# MAIN ------------------------------------------
if __name__ == "__main__": # sólo se ejecuta si abrimos este archivo directamente
    enviar_email(
        remitente = "example@mancheganfur.com",
        destinatario = "email@example.com",
        asunto = "Prueba",
        cuerpo = "Hola desde el código",
        password = "xxx"
    ) # llamada a la función correspondiente, con el envío de datos para enviar el correo