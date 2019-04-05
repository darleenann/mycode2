#!/usr/bin/env python3

import urllib.request
import json
import webbrowser

from pprint import pprint as pp # part of the standard library

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our api to call
MYKEY = 'api_key=88I4gpskgWmzqdgYSpWbedeQWmKuBFjxDQjgHgMI' ## this is my api key

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY)  # call the webservice
    nasaread = nasaapiobj.read()  # parse the JSON blob returned
    convertedjson = json.loads(nasaread.decode('utf-8'))  # convert json

    # show converted json
    print(convertedjson)  # show convereted JSON without pprint
    input('\nThis is converted json.  Press ENTER to continue.')  # pause for enter
    
    # Show Pretty Print json
    pp(convertedjson)  # this is pretty print in action

    #pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage input('\nThis is pretty printed JSON.  Press ENTER to continue.')  # pause for enter

    #Printe the description of the photo we are about to view
    print(convertedjson['explanation']) # display the value for the key explanation
    input('\nPress ENTER to view this photo of the day')  # open in the webbrowser

    webbrowser.open(convertedjson['hdurl']) # open in the webbrowser
main()
