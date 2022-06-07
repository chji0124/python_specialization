from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
'''
tags = soup('span')
for tag in tags:
    print('Contents:', tag.contents[0])
'''
# Retrieve all of the span tags
tags = soup('span')
sum = 0
numbers = list()
for tag in tags:
   num = tag.contents[0]
   sum = sum + int(num) 

print(sum)
