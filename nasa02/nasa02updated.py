#!/usr/bin/env python3

## this is the modern version of \nasa02\nasa02.py, written to observe BPs and use the requests library in contrast to using the urllib.request and the json (ie importing those two libraries, only the requests library is imported)

import requests ## 3rd party URL lookup

#define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' ## API URL
    startdate = 'start_date=2019-04-04'  ## start date for data
    enddate = '&end_date=END_DATE'       ## make a mechanism to utilize enddate
    mykey = '&api_key=88I4gpskgWmzqdgYSpWbedeQWmKuBFjxDQjgHgMI' ## my nasa dev key

    neourl = neourl + startdate + mykey
    print(neourl)


## Call the webservice
# neourlobj = urllib.request.urlopen(neourl)  ## Former url call

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()

## read the file-like object
#    neoread = neourlobj.read()

## decode json to python data structure
#    decodeneo = json.loads(neoread.decode('utf-8'))

## display our pythonic data
# print("\n\nConverted python data")
# print(decodeneo)

