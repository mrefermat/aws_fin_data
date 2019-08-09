from bs4 import BeautifulSoup
from urllib.request import urlopen

quote_page='http://archive.wortfm.org/'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

from mail import Email

msg=''
for l in soup.find_all(sho='83'): 
    msg=msg+ '<a href="' +  l.find('button').get('mp3') +  '">Diaspora</a>\n'


e=Email(subject='Weekly Update: Music Email')
e.add_text(msg)
e.send()
