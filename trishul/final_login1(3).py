#!/usr/bin/env python
#from http.cookies import *
import cgi
import sqlite3
import os
path='/var/www/html/07-10-15/project.db'
con=sqlite3.connect(path)
cur=con.cursor()
#d=SimpleCookie()
global n
def signup() :
    try:
        cur.execute("insert into student_list values(?,?,?,?,?,?,?)",(ROLL_NO,SECTION,n,SEMISTER,p,YEAR,BRANCH))
        cur.execute("insert into PROFILE VALUES(?,?,?,?)",(ROLL_NO,EMAIL_ID,GENDER,PHONE_NO))
        #cur.execute("INSERT INTO student values(?,?,?)",(ROLL_NO,p,'student'))
        con.commit()
    except Exception as e:
        print(e)    
form=cgi.FieldStorage()
print("Content-Type:text/html \n\n")
htmlFormat='''<html>
<head>
	<title>welcome to kmit</title>
	<link href="homepage_styles.css" type="text/css" rel="stylesheet" />
</head>
<body>
<center>
<form method="get" action="redirect.py">
<fieldset style="width:25%" >
<legend><h3><b>sign up</b></h3></legend>
<p>User ID:
<input type="text" name="username" size="15" maxlengh="30"/></p>
<p>Password:
<input type="password" name="password" size="15" maxlengh="30"/></p>
<p>Branch:
<input type="text" name="branch" size="15" maxlengh="30"/></p>
<p>Year:
<input type="text" name="year" size="15" maxlengh="30"/></p>
<p>Roll no:
<input type="text" name="roll_no" size="15" maxlengh="30"/></p>
<p>Gender:
<input type="text" name="gender" size="15" maxlengh="30"/></p>
<p>Semister:
<input type="text" name="semister" size="15" maxlengh="30"/></p>
<p>Section:
<input type="text" name="section" size="15" maxlengh="30"/></p>
<p>Email ID:
<input type="text" name="email_id" size="15" maxlengh="30"/></p>
<p>Phone No:
<input type="text" name="phone_no" size="15" maxlengh="30"/></p>
<a align="center"> <input type="submit" name="signup" value="signup"/></a>
</fieldset>
</form>
</center>

</body>
</html>'''
n=str(form.getvalue("username"))
p=str(form.getvalue("password"))
ROLL_NO=str(form.getvalue("roll_no"))
BRANCH=str(form.getvalue("branch"))
YEAR=str(form.getvalue("year"))
SEMISTER=str(form.getvalue("semister"))
SECTION=str(form.getvalue("section"))
EMAIL_ID=str(form.getvalue("email_id"))
PHONE_NO=str(form.getvalue("phone_no"))
GENDER=str(form.getvalue("gender"))
if 'signup' in form:
    signup()
print(htmlFormat.format(**locals()))




