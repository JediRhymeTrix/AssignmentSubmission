#!C:\Python34\python
import cgi
import sqlite3
import os
#from http.cookies import*
form = cgi.FieldStorage()

#path='/var/www/html/canteendb.db'
con=sqlite3.connect('canteendb.db')
cur=con.cursor()

#c=SimpleCookie()

curQ = 'Untitled-3.html'

print ("Content-type:text/html\r\n\r\n")

z =    """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="cssmenu/styles.css">
<title>assignment</title>
<style>
@import url(http://fonts.googleapis.com/css?family=Roboto:400,300,500);
</style>
<title>Untitled Document</title>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
<script src="jquery-linedtextarea.js"></script>
<link href="jquery-linedtextarea.css" type="text/css" rel="stylesheet" />
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
      <td><iframe name='question' width="600px" height="400px" src=%s></iframe></td>
      <td></td>
      <td>
         <form> <div id="t_area">Your Code Here:
            <textarea class="lined" rows="25" cols="100" name='answer' id='answer'>
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
<script>
$(function() {
    $(".lined").linedtextarea(
        {selectedLine: 1}
    );
});
</script>
<scrip src='../dist/autosize.js'>
</script>
<script>
        autosize(document.querySelectorAll('textarea'));
    </script>
</body>
</html>




""" #% ( curQ, )

'''
def toFile() :

	#string = form.getvalue('answer')
	print( form.getvalue('answer') )

	a = open ( 'C:\answer.py' , 'w' )
	a.write( string )

	a.close()
'''

if 'submit' in form :

	#string = form.getvalue('answer')

	a = open ( 'answer.py' , 'w' )
	a.write( form.getvalue('answer') )

	a.close()

else : a=open('answer2.py', 'w')

print (z)
	








'''

def session_in():
	cur.execute("insert into session values(?,?)",(hno,pwd))
	con.commit()
	
def register():
	cur.execute("insert into studentbase values(?,?,?,?,?)",(Roll,Name,Password,Mobile,Email))
	con.commit()
	os.system('/var/www/html/stud_reg_success.py')

def login():
	cur.execute("select roll,password from studentbase")
	temp=cur.fetchall()
	flag=0
	for i in temp:

		if i[0]==hno and i[1]==pwd:
			flag=1
			c['username']=hno            
			os.system('/var/www/html/stud_main.py')
			break
			
	if flag==0:
			os.system('/var/www/html/stud_login_fail.py')
			
			
	  
if form.getvalue('pwd') == form.getvalue('cpwd') :
		Name=form.getvalue('Name')
		Roll=form.getvalue('Roll_no')
		Password=form.getvalue('pwd')
		Mobile=form.getvalue('mobile')
		Email=form.getvalue('Email')
  
else :
	  os.system('/var/www/html/stud_login_reg_fail.py')
	  

if 'register' in form:
	register()
	
			  
   
 
hno=form.getvalue('@username')
pwd=form.getvalue('@password')




if 'login' in form :
		login()


if Name == None and hno==None :
		print(z)
con.close()

print(c.js_output())

'''
