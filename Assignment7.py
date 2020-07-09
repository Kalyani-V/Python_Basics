###############
####Python for Informatics
####Assignment 7 - Alpha-Vantage
###############

import sys
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Your key here
api_key = 'XOORBWLXMXPLYFGC'
if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://www.alphavantage.co/query?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

status = True

while status:
    symbol =input("Enter Symbol : ")
    if len(symbol)<1:
        break
    parms=dict()
    parms['function'] = "GLOBAL_QUOTE"
    parms['symbol'] = symbol

    if api_key is not False:
        parms['apikey'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)
    # print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    # print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
        price = js["Global Quote"]["05. price"]
        # print(json.dumps(js, indent=4))
        print("Price of an item is :",price)
    except:
        print("There is no price for that stock")

    input_status=input("Do you want to continue : Y/N -")
    if input_status=="Y":
        status = True
    elif input_status=="N":
        status = False
    else:
        print("Wrong choice. Quiting")
        status = False
sys.exit()