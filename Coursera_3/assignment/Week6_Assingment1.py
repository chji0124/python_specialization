from typing import Any
import urllib.request, urllib.parse, urllib.error
import json
#use built-in json libary to parse the JSON and read through the data
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
uhandle = urllib.request.urlopen(url, context=ctx)

data = uhandle.read()
print('Retrieving', url) 
print('Retrieved', len(data), 'characters')

info = json.loads(data) #
print('Count:', len(info))
#print(info["comments"]) #multiple dictionaries in a list

information = info["comments"] #information is a list of comment
print(information)
sum = 0

for comment in information: #for each comment in information
    num = comment["count"]
    sum = sum + int(num)

print(sum)







    
    
