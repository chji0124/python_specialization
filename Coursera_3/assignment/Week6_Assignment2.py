import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    # base url

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True: #why using WHILE STATEMENT; you can input infinite address
    address = input('Enter location: ') 
    if len(address) < 1: break

    parameters = dict()
    parameters['address'] = address
    if api_key is not False: parameters['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parameters)
    #url = 'http://py4e-data.dr-chuck.net/json?address=abc&number=123'

    print('Retrieving', url)
    uhandler = urllib.request.urlopen(url, context=ctx)
    data = uhandler.read().decode() #collecting the data; after decoding it will become a string
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) #read the data and deserialize to a python object
    except:
        js = None
    #**error handling**; your load can have error and can blow up; if you do not use (try,except), program might die
    #only way python can check errors

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    place = js['results'][0]['place_id']
    print('Place id', place)
    