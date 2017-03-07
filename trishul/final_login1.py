#!/usr/bin/env python
#from http.cookies import *
import cgi
import sqlite3
import os
path='/var/www/html/done/project.db'
con=sqlite3.connect('project.db')
cur=con.cursor()
#d=SimpleCookie()
global NAME
def signup() :
    cur.execute("INSERT INTO student values(?,?,?)",(ROLL_NO,PASSWORD,'student'))
    cur.execute("insert into student_list values(?,?,?,?,?,?,?)",(ROLL_NO,SECTION,NAME,SEMISTER,PASSWORD,YEAR,BRANCH))
    cur.execute("insert into PROFILE VALUES(?,?,?,?)",(ROLL_NO,EMAIL_ID,GENDER,PHONE_NO))
    #cur.execute("INSERT INTO student values(?,?,?)",(ROLL_NO,PASSWORD,'student'))
    con.commit()
    print(onSignUp)

onSignUp='''<html>
<body onload="window.location='http://127.0.0.1/done/final_login.py'">
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
  <input name='username' placeholder='Username' type='text' required>
  <input id='pw' name='password' placeholder='Password' type='password' required>
  <input name='email' placeholder='E-Mail Address' type='text'>
  <input name='roll_no' placeholder='ROLL_NO' type='text'>
  <input name='branch' placeholder='BRANCH' type='text'>
  <input name='year' placeholder='YEAR' type='text'>
  <input name='semister' placeholder='SEMISTER' type='text'>
  <input name='section' placeholder='SECTION' type='text'>
  <input name='Gender' placeholder='GENDER' type='text'>
  <input id="phone" name="phone" placeholder="phone number" required="" type="text"> <br><br>

  <input class='animated' type='submit' value='Sign Up' name='signup' >

  </form>
  <a class='forgot' href='#'>Already have an account?</a>
</div>
</body>

</html>





'''
NAME=str(form.getvalue("username"))
PASSWORD=str(form.getvalue("password"))
ROLL_NO=str(form.getvalue("roll_no"))
BRANCH=str(form.getvalue("branch"))
YEAR=str(form.getvalue("year"))
SEMISTER=str(form.getvalue("semister"))
SECTION=str(form.getvalue("section"))
EMAIL_ID=str(form.getvalue("email"))
PHONE_NO=str(form.getvalue("phone"))
GENDER=str(form.getvalue("Gender"))

if 'signup' in form:
    signup()


#if(signup() == 1): print(onSignUp)

print(htmlFormat.format(**locals()))




