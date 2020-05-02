from bs4 import BeautifulSoup
from urllib.request import urlopen
from mail import Email

quote_page='http://archive.wortfm.org/'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

msg=''
for l in soup.find_all(sho='83'): 
    msg=msg+ '<p><a href="' +  l.find('button').get('mp3') +  '">Diaspora</a>'

for l in soup.find_all(sho='72'): 
    msg=msg+ '<p><a href="' +  l.find('button').get('mp3') +  '">Global Revolution</a>'

for l in soup.find_all(sho='21'): 
    msg=msg+ '<p><a href="' +  l.find('button').get('mp3') +  '">Entertainment</a>\n'

for l in soup.find_all(sho='62'): 
    msg=msg+ '<p><a href="' +  l.find('button').get('mp3') +  '">Journeys Into Jazz</a>\n'

for l in soup.find_all(sho='43'): 
    msg=msg+ '<p><a href="' +  l.find('button').get('mp3') +  '">Something Wonderful</a>\n'

e=Email(subject='Weekly Update: Music Email',to=['mark.refermat@gmail.com'])
e.add_text(msg)
e.send()
