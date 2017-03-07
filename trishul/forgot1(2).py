#!/usr/bin/env python3



#REQUIRED FOR INTEGRATING EMAIL
import smtplib
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import email.mime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yagmail



import cgi
import sqlite3
import cgitb; cgitb.enable()
import time
import random



yag = yagmail.SMTP('dummy.trishul@gmail.com', 'bilbobaggins')
yag.send('vshah9031@gmail.com', subject = test, contents = 'abcdefg')



#FOR GENERATING RANDOM NUMBER
def rand():
    global rnd
    rnd=str(random.randint(100000,999999))

    
#FOR INSERTING A RANDOM NUMBER AS PASSWORD INTO THE DATABASE
def ins():
    global to
    print(to)
    cur.execute("UPDATE staff SET password=? WHERE email_id=?", (rnd,to))
    con.commit()
   
#FOR SMS
'''def sms():
    from getpass import getpass
    import sys
    import nsm2
    
    def smsinvgp(u,p,rm):
        global user
        global pwd1
        global msg1
        global rcmobile
        user=u
        pwd1=p

        
        #EXTRACTING MOBILE NUMBER
        temp3='select mob from staff where email="'+to+'"'
        cur.execute(temp3)
        temp3=cur.fetchall()
        
        msg1='Dear User,Your Password has been reset to know your New Password.Please check your Email.'
        rcmobile=rm
        nsm2.smscall('8686956567','rajrocks',msg1,str(temp3[0][0]))
    smsinvgp('9573205741','T6329H',12)'''

    
    
#FUNCTION FOR EMAIL
def email():
                
    fromaddr = "dummy.trishul@gmail.com"

    #GENERATING MESSAGE IN EMAIL
    
    
    body='Dear User,Your Password has been reset to '+rnd+' .Please Login with your New Password'
    subj="Password Issue"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = to
    msg['Subject'] = subj
     
     
    msg.attach(MIMEText(body, 'plain'))
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,"bilbobaggins")
    text = msg.as_string()
    server.sendmail(fromaddr, to, text)
    server.quit()









#CONNECTING DATABASE
path="/var/www/html/done/project.db"
con=sqlite3.connect(path)
cur=con.cursor()


form=cgi.FieldStorage()
print("Content-type:text/html\r\n\r\n")
htmlFormat="""
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to KMIT trishul</title>
    <link rel="stylesheet" type="text/css" href="text.css" />
</head>
<body>
    
                            <h3>FORGOT PASSWORD</h3>
                            <form>
                            <table align="center">
<tr><td><input type="text" name="username" required placeholder="Email"></input></td></tr>
<tr><td><input type="submit" name="get" value="Get Password" ></input></td</tr></table></form>
</body></html>"""
to=str(form.getvalue("username"))

print (form)

if "get" in form:
    rand()
    ins()
    email()
print(htmlFormat.format(**locals()))
				
				
		
