#!/usr/bin/env python
#from http.cookies import *
import cgi
import sqlite3
import os
path='/var/www/html/done/project.db'
con=sqlite3.connect(path)
cur=con.cursor()
#d=SimpleCookie()
global ROLL_NO
def login():
        try:
                
                print("in login")
                cur.execute("select * from student")
                a=cur.fetchall()
                f=0
                for i in a:
                        
                    if(ROLL_NO==i[0] and PASSWORD==i[1]):
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
<body onload ="window.location='faculty_page.html'">
</body>
</html>'''
hadmin='''<html>
<body onload ="window.location='http://127.0.0.1/admin_page.py'">
</body>
</html>'''
htmlFormat='''<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Sofia' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="text1.css"/>

<div id="nav">                                
				<div id="navItem1">
					<a href="">Student</a>
				</div>
				<div id="navItem2">
					<a href="">Staff </a>
				</div>
				<div id="navItem3">
					About Us
				</div>
				<div id="navItem4">
					<a href="">Contact Us</a>
				</div>


<div class='login'>
  <h2>Login</h2>
  <form method="get" >
  <input name='username' placeholder='ROLL_NO' type='text' required/>
  <input id='pw' name='password' placeholder='Password' type='password' required/><br><br>
  <input class='animated' type='submit' name='login' value='Login' ><br><br>
</form>
  <form method="get" action='final_login1.py'>
  <input class='animated' type='submit' name='sign_up' value='Sign Up' >
  <a class='forgot' href='#'>Forgot Password?</a> 
</form>
</div>  



</body>
</html>'''
ROLL_NO=str(form.getvalue("username"))
PASSWORD=str(form.getvalue("password"))
if 'login' in form:
    login()

print(htmlFormat.format(**locals()))

