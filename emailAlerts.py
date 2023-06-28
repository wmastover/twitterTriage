import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText  # import MIMETex
from email import encoders

def sendEmail(subject, body, filename):
        
    appPassword = 

    connection = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    email_addr = 'frontdooremma@gmail.com'
    email_passwd = appPassword
    connection.login(email_addr, email_passwd)

    msg = MIMEMultipart()
    msg['From'] = email_addr
    msg['To'] = 'will@frontdoor.xyz'
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))

    if filename != "":

        attachment = open(filename, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

    text = msg.as_string()
    connection.sendmail(email_addr, 'will@frontdoor.xyz', text)
    connection.close()

