#!/usr/bin/env python3

import urllib.request
import json

#define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-07-04'
enddate = '&end_date=END_DATE'
mykey = '&api_key=88I4gpskgWmzqdgYSpWbedeQWmKuBFjxDQjgHgMI' ## my nasa dev key

neourl = neourl + startdate + mykey
print(neourl)

## Call the webservice
neourlobj = urllib.request.urlopen(neourl)

## read the file-like object
neoread = neourlobj.read()

## decode json to python data structure
decodeneo = json.loads(neoread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeneo)

