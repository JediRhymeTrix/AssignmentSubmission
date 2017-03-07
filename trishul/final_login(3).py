#!/usr/bin/env python
#from http.cookies import *
import cgi
import sqlite3
import os
path='/var/www/html/07-10-15/project.db'
con=sqlite3.connect('project.db')
cur=con.cursor()
#d=SimpleCookie()
global n
def login():
        try:
                
                print("in login")
                cur.execute("select * from student")
                a=cur.fetchall()
                f=0
                for i in a:
                        
                    if(n==i[0] and p==i[1]):
                        print('login successful')
                        #d['username']=n
                        #print(d.js_output());
                        z=str(i[2])
                        if(z=='student'):
                            print(stu)
                        if(i[2]=='faculty'):
                            print(facultyh)
                        if(i[2]=='admin'):
                            print(hadmin)
                        f=1
                if(f==0):
                    print("loginfailed")
        except Exception as e:
                print(e)
form=cgi.FieldStorage()
print("Content-Type:text/html \n\n")
stu='''<html>
<body onload ="window.location='student_page.html'">
</body>
</html>'''
facultyh='''<html>
<body onload ="window.location='http://127.0.0.1/faculty_page.py'">
</body>
</html>'''
hadmin='''<html>
<body onload ="window.location='http://127.0.0.1/admin_page.py'">
</body>
</html>'''
htmlFormat='''<html>
<head>
	<title>welcome to kmit</title>
	<link href="homepage_styles.css" type="text/css" rel="stylesheet" />
</head>
<body>

<center>		
<form>
<fieldset style="width:25%" >
<legend><h3><b>Login</b></h3></legend>
<p>User ID:
<input type="text" name="username" size="15" maxlengh="30"/></p>
<p>Password:
<input type="password" name="password" size="15" maxlengh="30"/></p>
<a align="center"> <input type="submit" name="login" value="login"/></a>
</fieldset>
</form>
</center>



</body>
</html>'''
n=str(form.getvalue("username"))
p=str(form.getvalue("password"))
if 'login' in form:
    login()

print(htmlFormat.format(**locals()))

