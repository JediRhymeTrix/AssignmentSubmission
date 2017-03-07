#!/usr/bin/env python3
import smtplib
import cgi
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import email.mime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
form=cgi.FieldStorage()
def email1():
    try:
       
        fromaddr = "kmitpython21@gmail.com"
        #toaddr = "sivamanchala@gmail.com"
        global fadr
        global tadr
        global subj
        global ftype
        global f1
        
        msg = MIMEMultipart()
         
        msg['From'] = fadr
        msg['To'] = tadr
        #msg['Subject'] = "SUBJECT OF THE EMAIL"
        msg['Subject'] = subj
         
        body = "TEXT YOU WANT TO SEND"
         
        msg.attach(MIMEText(body, 'plain'))
         
        filename = ftype
        #attachment = open("/var/www/html/hello.py", "rb")
        if(f1==None):
            print("please select the file....")
        else:
            attachment = open(f1, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
         
        msg.attach(part)
         
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        #server.login(fromaddr, "advaith13")
        server.login(fadr, "kmit@python21")
        text = msg.as_string()
        #server.sendmail(fromaddr, toaddr, text)
        server.sendmail(fadr, tadr, text)
        server.quit()
    except Exception as e:
        print(e)
print("Content-Type: text/html\n\n")  # html markup follows


htmlFormat = """
<html>
  <Title>Email</Title>
<body>
<form>
From:<input type='text' name='from' value=0 autofocus> </input></br>
To:<input type='text' name='to' value=0 > </input></br>
subject:<input type='text' name='sub' value=0 ></br>
file_name:<input type='text' name='fltype' value=0 ></input></br>
<p>File: <input type="file" name="filename" value=0/> </input></p></br>

<input type='submit' name='sendmail' value='upload'></input></br>

</form>
  
  <p> message has been sent to: {tadr}</p>
  
</body>
</html> """
fradr=form.getvalue('from',0)
toadr=form.getvalue('to',0)
subj=form.getvalue('sub',0)
ftype=form.getvalue('fltype',0)
smsg=form.getvalue('msg',0)
f1=form.getvalue('filename',0)
fadr=str(fradr)
tadr=str(toadr)
if "sendmail" in form:
    email1()
   
print(htmlFormat.format(**locals())) 
