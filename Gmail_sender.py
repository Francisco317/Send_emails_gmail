
#IMPORTACION DE LAS PAQUETERIAS 
from email.message import EmailMessage
import ssl
import smtplib
import csv 

#INFORMACION DEL EMISOR DEL CORREO
#SE REQUIERE ACTIVAR VERIFICACION DE 2 PASOS EN GMAIL PARA OBTENER CONTRASEÑA
email_emisor = "colaboradorgm1@gmail.com"
email_contrasena = "rlesbmmgbviufztt"

#ASUNTO DEL MENSAJE, SE CREA LA VARIABLE PARA DESPUÉS MANDARLA TRAER"
asunto = "Buenos días compañero"


#AQUI MANDAMOS A TRAER EL ARCHIVO CSV Y DE DONDE SALDRA LA INFORMACION
with open('Workers.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    #ESTE FOR HARA QUE SE ENVIEN LOS MENSAJES DE TODOS LOS REGISTROS EN EL CSV HASTA EL ULTIMO
    for row in csv_reader:                      
        

        #CONTENIDO DEL MENSAJE"
        cuerpo = (f'{row["Nombre"]} trabaja en el departamento de {row["Departamento"]}, nacio en el mes de {row["Mes cumple"]}, y su correo es:{row["email"]}.')

        #INFORMACIÓN SOBRE EL DESTINATARIO Y QUE VA A IR EN EL ASUNTO Y CONTENIDO
        email_receptor = (f'{row["email"]}')
        em = EmailMessage()
        em["From"] = email_emisor
        em["To"] = email_receptor
        em["Subject"] = asunto
        em.set_content(cuerpo)

        contexto = ssl.create_default_context()

        #AQUI CON SMTPLIB ES DONDE SE ENVIA EL CORREO CON LA INFORMACION ANTERIOR
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
            smtp.login(email_emisor, email_contrasena)

            smtp.sendmail(email_emisor, email_receptor, em.as_string())

            smtp.quit()
    
