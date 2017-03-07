#!/usr/bin/env python3
#from http.cookies import *
import cgi
import sqlite3
import os
import yagmail
global to
to='sairaghuram123@gmail.com'

path='/var/www/html/done/project.db'
con=sqlite3.connect(path)
cur=con.cursor()

curQ = 'text.txt'
form=cgi.FieldStorage()

print("Content-Type:text/html\n\n")

html='''<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>assignment</title>
<style>
@import url(http://fonts.googleapis.com/css?family=Roboto:400,300,500);
</style>
<title>Untitled Document</title>

<style>
body {
    background-color: #F2F2F2
}
table {
    margin: 100;
    width: 100%;
}
div#t_area {
    background-color: #333549;
 background-color: #;
    color: #DDDDDD;
    box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, 0.2);
}
textarea {
    background-color: #333549;
    color: #DDDDDD;
    width: 100%;
    box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, 0.2);
}
iframe {
    box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, 0.2);
}
input.submit {
    box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, 0.2);
}
input.submit: {
 box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, 0.2);
}
</style>
</head>
<body>
<table>
  <tbody>
    <tr>Question:
      <td><iframe name='question' width="600px" height="400px" src='''+curQ+'''></iframe></td>
      <td></td>
      <td>
          <div id="t_area">Your Code Here:
            <form><textarea class="lined" rows="25" cols="100" name='answer' id='answer'>
JavaScript was originally developed by Brendan 
Eich of Netscape under the name Mocha, 
which was later renamed to LiveScript, 
and finally to JavaScript. 

The change of name from LiveScript to JavaScript roughly 
coincided with Netscape adding support for 
Java technology in its Netscape Navigator 
web browser. 

JavaScript was first introduced 
and deployed in the Netscape browser version 
2.0B3 in December 1995. 

The naming has caused confusion, giving the 
impression that the language is a spin-off of Java, 
and it has been characterized by many as a 
marketing ploy by Netscape to give JavaScript the 
cachet of what was then the hot new web-programming language.

</textarea>
          </div>
          <input class="submit" type='submit' name='submit' onClick=init()/>
        </form></td>
    </tr>
  </tbody>
</table>

</body>
</html>'''

if 'submit' in form :
        
	#string = form.getvalue('answer')

	a = open ( 'answer.py' , 'w' )
	a.write( form.getvalue('answer') )

	a.close()
	yag = yagmail.SMTP('dummy.trishul@gmail.com', 'bilbobaggins').send(to, subject = None, contents = 'answer.py')


else : a=open('answer2.py', 'w')

print(html)
