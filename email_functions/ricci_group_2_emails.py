import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import  pandas as pd

def ricci_sender_2(df,type):

    #Cargar contraseña del correo Ricci
    config = configparser.ConfigParser()
    config.read_file(open('email.cfg'))
    user = config.get('EMAIL', 'user')
    password = config.get('EMAIL', 'password')

    #Set email user and pass for group 1 ricci
    gmail_user = user
    gmail_pass = password

    #Cargar correos estudiantes y crear la lista
    df_students = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTivwaP50iSjwzM5a7cHcctz51XfOTONPrfURP6hcruTesIhtMe0ZSF6mHVgqA6ygYwhCByIU-Qsyke/pub?gid=0&single=true&output=csv')
    gmail_destination = df_students['CORREO'].tolist()
    #gmail_destination = 'ing.danielarroyave@gmail.com'


    # Create message and embed dataframe as html
    msg = MIMEMultipart()
    msg['Subject'] = type

    html = """\
                    <html>
                      <head></head>
                      <body>

                        <p>Hola! A continuación las señales del dia, ten en cuenta que el correo puede llegar varias veces. <br>

                        <p>{0}</p>

                        La presente alerta no representa una recomendación de inversión.

                        <p>Cada operador debe tomar sus propias decisiones de acuerdo a su análisis y control del riesgo.</p>
                        </p>
                      </body>
                    </html>
                    """.format(df.to_html(index=False, justify='center'))

    part1 = MIMEText(html, 'html')

    msg.attach(part1)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.sendmail(gmail_user, gmail_destination, msg.as_string())
    server.quit()