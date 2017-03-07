#!/usr/bin/env python
#from http.cookies import *
import cgi
import sqlite3
import os
path='/var/www/html/project.db'
con=sqlite3.connect(path)
cur=con.cursor()
#d=SimpleCookie()
global n
def login():
        try:
                
                print("in login")
                for i
                cur.execute("select * from student_list")
                a=[]
                a=cur.fetchall()
                print(a)
                f=0
                data1=[]
                for i in a:
                        
                    if(n==i[0] and p==i[4]):
                        print('login successful')
                        #d['username']=n
                        #print(d.js_output());
                        z=i[9]
                        '''cur.execute("select ROLL_NO from student_list where student_list.ROLL_NO=n")
                        data1=cur.fetchall()
                        print(data)
                        con.commit()
                        cur.execute("select staff_id from staff where staff.staff_id=n")
                        data2=cur.fetchall()
                        con.commit()
                        cur.execute("select admin_id from admin where admin.admin_id=n")
                        data3=cur.fetchall()
                        con.commit()'''
                        if(i[9]=='student'):
                            print(stu)
                        if(i[9]=='faculty' ):
                            print(facultyh)
                        if(i[9]=='admin'):
                            print(hadmin)    
                        f=1
                if(f==0):
                    print("loginfailed")
        except Exception as e:
                print(e)
form=cgi.FieldStorage()
print("Content-Type:text/html \n\n")
stu='''<html>
<body onload ="window.location='http://127.0.0.1/student_page.py'">
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
<fieldset style=
"width:25%" >
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

