import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


email_user = 'gmail@gmail.com' # enter gmail
email_send = 'gmail@gmail.com' # confirmation gmail
subject = 'Python'


msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject


body = 'Hi there, sending this'
msg.attach(MIMEText(body, 'plain'))


filename = 'new.txt' # The file that will be sent 
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename"+filename)


msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_send, 'password') # enter password


server.sendmail(email_user,email_send,text)
server.quit()