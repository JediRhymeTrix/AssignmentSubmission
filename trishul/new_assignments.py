#!/usr/bin/env python3
#from http.cookies import *
import cgi
import sqlite3
import os
path='/var/www/html/done/project.db'
con=sqlite3.connect(path)
cur=con.cursor()
form=cgi.FieldStorage()
#url=str(form.getvalue("url"))
#print (url)
    

    

print("Content-Type:text/html\n\n")

html='''
<html>
<head>
<meta charset="utf-8">
<title>New Assignment</title>
</head>

<body>
<h1>New Assignment: </h1>

<form style="display: block;">
<table>
<tbody>
<tr>
<td>Title : <input type="text" name="title"></input></td></tr>
<tr><td>Due Date : <input type="date" name="due" /></td></tr>
<tr><td>URL : <input type="url" name="url"></input></td></tr>
<tr><td>(OR)</td></tr>
<tr><td>Upload : <input type="file" name="file"></input> </td></tr>
<tr><td><input type="submit" name="submit" value="submit"/></td></tr>
</form>
</tbody></table>

</body>
</html>'''

title=str(form.getvalue("title"))
due=str(form.getvalue("due"))
url=str(form.getvalue("url"))

if "submit" in form:
    if "file"in form:
        print(form.getvalue("file"))
        

    cur.execute("insert into assignments values(?,?,?,?,?,?)",('1',title,'None',due,'python',url))
    con.commit()

print(html)
