#REQUIRED FOR INTEGRATING EMAIL
import smtplib
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import email.mime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    #FUNCTION FOR EMAIL
    def email1(self,body,toaddr,subj):
        fromaddr = "kmitgatepass@gmail.com"  
        
        msg = MIMEMultipart()
         
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subj
         
         
        msg.attach(MIMEText(body, 'plain'))
         
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "kmit@gate")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
email3=Email()
