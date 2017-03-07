#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
from datetime import datetime

try:
    # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
    
except ImportError:
    pass
form = cgi.FieldStorage()
print("Content-Type: text/html\n\n")
html="""
<html>
<body>
<form enctype="multipart/form-data" action="" method="post">
<p>File: <input type="file" name="file"></p>
<p><input type="submit" value="Upload" name="upload"></p>
</form>
<p></p>
</body>
</html>
"""
if "upload" in form:

    assno = 1
    track = "Python"
    rollNo = "54c"

    date = datetime.now()
    curDate = date.strftime('%Y-%m-%d')
    
    #fileitem=form['file']
    # A nested FieldStorage instance holds the file
    fileitem = form.getvalue("file")
    # Test if the file was uploaded
    if fileitem:
       # strip leading path from file name to avoid directory traversal attacks
       fn = assno+'_'+track+'_'+rollNo
       #print(fn)
       open(fn+'.doc', 'wb').write(fileitem)
       #print( 'The file "' + fn + '" was uploaded successfully' )
       print( 'The file was uploaded successfully' )
    else:
       print('No file was uploaded')
   

print(html.format(**locals()))
