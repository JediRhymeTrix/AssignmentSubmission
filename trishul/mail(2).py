import yagmail
yag = yagmail.SMTP('vedant.vohra1@gmail.com', 'busbuddies')
yag.send('sairaghuram123@gmail.com', subject = None, contents = 'Hello')

'''

(OR)

import yagmail
yag = yagmail.SMTP()
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('to@someone.com', 'subject', contents)

'''
