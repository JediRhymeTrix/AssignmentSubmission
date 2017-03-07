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


print ("Content-Type:text/html\r\n\r\n")

z =    """

<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Material Design Floating Input Placeholder DEMO</title>
<link href="http://www.cssscript.com/wp-includes/css/sticky.css" rel="stylesheet" type="text/css">
<link href="http://fonts.googleapis.com/css?family=Roboto:400' rel='stylesheet" type='text/css'>
<style class="cp-pen-styles">
h1, input::-webkit-input-placeholder, button {
 font-family: 'roboto', sans-serif;
 -webkit-transition: all 0.3s ease-in-out;
 transition: all 0.3s ease-in-out;
}

h1 {align
  height: 100px;
  width: 100%;
  font-size: 18px;
  background: #18aa8d;
  color: white;
  line-height: 150%;
  border-radius: 3px 3px 0 0;
  box-shadow: 0 2px 5px 1px rgba(0, 0, 0, 0.2);
}

form {
  box-sizing: border-box;
  width: 260px;
  margin: 150px auto 0;
  box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, 0.2);
  padding-bottom: 0.09px;
  border-radius: 3px;
}

form h1 {
  box-sizing: border-box;
  padding: 20px;
}

input {
  margin: 40px 25px;
  width: 200px;
  display: block;
  border: none;
  padding: 10px 0;
  border-bottom: solid 1px #1abc9c;
  -webkit-transition: all 0.3s cubic-bezier(0.64, 0.09, 0.08, 1);
  transition: all 0.3s cubic-bezier(0.64, 0.09, 0.08, 1);
  background: -webkit-linear-gradient(top, rgba(255, 255, 255, 0) 96%, #1abc9c 4%);
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 96%, #1abc9c 4%);
  background-position: -200px 0;
  background-size: 200px 100%;
  background-repeat: no-repeat;
  color: #0e6252;
}
input:focus, input:valid {
 outline: none;
 background-position: 0 0;
}
input:focus::-webkit-input-placeholder, input:valid::-webkit-input-placeholder {
 color: #1abc9c;
 font-size: 11px;
 -webkit-transform: translateY(-20px);
 transform: translateY(-20px);
 visibility: visible !important;
}

.button {
  border: none;
  background: #1abc9c;
  cursor: pointer;
  border-radius: 3px;
  padding: 6px;
  width: 200px;
  color: white;
  margin-left: 25px;
  box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.2);
}

.button:hover {
  -webkit-transform: translateY(-3px);
  -ms-transform: translateY(-3px);
  transform: translateY(-3px);
  box-shadow: 0 6px 6px 0 rgba(0, 0, 0, 0.2);
}
</style>
</head>

<body>

<form method="POST">
  <h1> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; STUDENT LOGIN</h1>
  <input name="username" placeholder="Username" type="text" required>
  <input name="password" placeholder="Password" type="password" required>
  <input type="submit" name='login' value="Login" class="button" /></input>

</body>
</html>


"""

'''
def register() :

    cur.execute("INSERT INTO studentbase values(?,?,?,?,?)",(Roll,Name,Mobile,Email))

    con.commit()
    con.close()
    

'''

def login():
        try:
                
                print("in login")
                cur.execute("select * from student_list")
                a=cur.fetchall()
                f=0
                for i in a:
                        
                    if(n==i[0] and p==i[4]):
                        print('login successful')
                        #d['username']=n
                        #print(d.js_output());
                        cur.execute("select ROLL_NO from student_list where student_list.ROLL_NO=n")
                        data1=cur.fetchall()
                        con.commit()
                        cur.execute("select staff_id from staff where staff.staff_id=n")
                        data2=cur.fetchall()
                        con.commit()
                        cur.execute("select admin_id from admin where admin.admin_id=n")
                        data3=cur.fetchall()
                        con.commit()
                        if(i[0]==data1[0][0]):
                            print("student login")
                        if(i[0]==data2[0][0] ):
                            print("staff login")
                        if(i[0]==data3[0][0]):
                            print("admin login")    
                        f=1
                if(f==0):
                    print("loginfailed")
        except Exception as e:
                print(e)
                    
                
n=str(form.getvalue("username"))
p=str(form.getvalue("password"))
if 'login' in form:
    login()


print(z)
