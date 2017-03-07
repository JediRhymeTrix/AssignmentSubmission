#!/usr/bin/env python
#from http.cookies import *
import cgi
import sqlite3
import os
#import yagmail
import random1

path='/var/www/html/done/project.db'
con=sqlite3.connect('project.db')
cur=con.cursor()
#d=SimpleCookie()
global NAME
def signup() :
    try:
        cur.execute("INSERT INTO staff values(?,?,?,?,?,?)",(STAFF_ID,NAME,EMAIL_ID,PHONE_NO,'None',TRACK))
        cur.execute("INSERT INTO student values(?,?,?)",(STAFF_ID,'None','faculty')) 
    
        con.commit()
        print(SignUp)
        #rnd="abcdefg"

        #yag = yagmail.SMTP('dummy.trishul@gmail.com', 'bilbobaggins').send('sairaghuram123@gmail.com', subject = Test, contents = rnd)
        
    except:
        print("error")
          
    #print(onSignUp)

onSignUp='''<html>
<body onload="window.location='http://127.0.0.1/done/final_login.py'">
</body>
</html>'''
SignUp='''<html>
<body onload="window.location='http://127.0.0.1/done/forgot.py'">
</body>
</html>'''

form=cgi.FieldStorage()
print("Content-Type:text/html \n\n")
htmlFormat='''<html>
<head>
<meta charset="utf-8">
<title>Untitled Document</title>
<link href="text.css" rel="stylesheet" type="text/css">
</head>

<body>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Sofia' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="text.css"/>
<div class='login'>
  <h2>Sign Up</h2>
  <form method="get" >
  <input name='username' placeholder='NAME' type='text' required>
  <input name='staff_id' placeholder='STAFF_ID' type='text' required>
  <input name='email' placeholder='E-Mail Address' type='text'>
  <input name='track' placeholder='TRACK' type='text'>
  
  <input name="phone" placeholder="phone number" required="" type="text"> <br><br>

  <input class='animated' type='submit' value='Sign Up' name='signup' >

  </form>
  <a class='forgot' href='#'>Already have an account?</a>
</div>
</body>

</html>





'''
NAME=str(form.getvalue("username"))
STAFF_ID=str(form.getvalue("staff_id"))
EMAIL_ID=str(form.getvalue("email"))
PHONE_NO=str(form.getvalue("phone"))
TRACK=str(form.getvalue("track"))

if 'signup' in form:
    signup()


#if(signup() == 1): print(onSignUp)

print(htmlFormat.format(**locals()))



