#!/usr/bin/env python3
#from http.cookies import *
import cgi
import sqlite3
import os
path='/var/www/html/done/project.db'
con=sqlite3.connect(path)
cur=con.cursor()
form=cgi.FieldStorage()
print("Content-Type:text/html\n\n")

stu='''<html>
<link rel="stylesheet" href="/var/www/html/done/styles.css">
<body>
<iframe name='question' width=500 height=300 src=%s></iframe>
<form>
	<textarea name='answer' id='answer' cols=69 rows=20></textarea>
	<input type='submit' name='submit' value='submit'></input>
</form>
</body>
</html>'''

if 'submit' in form :

	#string = form.getvalue('answer')

	a = open ( 'answer.py' , 'w' )
	a.write( form.getvalue('answer') )

	a.close()

else : a=open('answer2.py', 'w')


#if 'login' in form:
#    login()
print(stu)
#print(stu.format(**locals()))
