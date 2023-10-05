import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


fromaddr = 'fomina.katrine@mail.ru'
toaddr = 'fomina.katrine@mail.ru'
mypass = 'eb4BB6DdiN2qCEPzzA73'
reportname = 'log.txt'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'отчет от питона'
text = 'отчет от питона log.txt'

msg.attach(MIMEText(text))

with open(reportname, 'rb') as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = 'attachment; filename="{basename(reportname)}"'
    msg.attach(part)

# body = 'тестовое сообщение'
# msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


