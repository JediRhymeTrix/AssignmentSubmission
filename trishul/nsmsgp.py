#!/usr/bin/env python3
from getpass import getpass
import sys
import cgi
import nsm2
#import urllib3.
form=cgi.FieldStorage()
'''def smsinv():
    global user
    global pwd1
    global msg1
    global rcmobile
    print("in sms inv",user)
    nsm2.smscall(user,pwd1,msg1,rcmobile)'''
def smsinvgp(u,p,m,rm):
    try:
        global user
        global pwd1
        global msg1
        global rcmobile
        user=u
        pwd1=p
        msg1=m
        rcmobile=rm
        #print("in smsinvgrp")
        print("\n\n\n\n\n\n\n usr",user,pwd1,rcmobile)
        #print("in sms inv",moblist)
        '''for mob in moblist:
            print(mob)'''
        nsm2.smscall(user,pwd1,msg1,rcmobile)
    except Exception as e:
        print(e)
    
print("Content-Type:text/html\n\n")
html='''
<html>
<body>
<head><title>sms</title><link rel="stylesheet" type="text/css" href="index.css"></head>
<form>
username:<input type="text" name="usr" value="9573205741" autofocus></input></br>
password:<input type="password" name="pwd" value="T6329H"></input></br>
message:<input type="textarea" name="msg" value="hi"></input></br>
receiver-mobile:<input type="text" name="rmobile" value="0"></input></br>

    <input type="submit" name="click" value="send"></input>
</form>
<p> message has been sent to: {rcmobile}</p>
</body>
</html>'''

user=str(form.getvalue("usr",'9573205741'))
pwd1=str(form.getvalue("pwd",''))
msg1=str(form.getvalue("msg",''))
rcmobile=str(form.getvalue("rmobile",''))
#mobile=int(rcmobile)

if "click" in form:
    #smsinv()
    moblist=rcmobile.split(',')
    print("list",moblist)
    #for mob in moblist:
    #print("mob:",mob)
    smsinvgp(user,pwd1,msg1,moblist[0])
    smsinvgp(user,pwd1,msg1,moblist[1])
print(html.format(**locals()))
#print(html)

