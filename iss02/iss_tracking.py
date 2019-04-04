#!/usr/bin/env

import urllib.request
import json
import turtle
import time

## trace the ISS - earth-orbital space station 
eoss = 'http://api.open-notify.org/iss-now.json'

print('this is the contents for variable for eoss:' + eoss)

# call the webserver
trackiss = urllib.request.urlopen(eoss)

print('this is the variable contents for trackiss:', trackiss)

#put into file object
ztrack = trackiss.read()

print('this is the contents of the variable ztrack: {}'.format(ztrack))

## jason 2 python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(result)
input('\nIss data retrieved & converted.  Press any key to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('longitude: ', lon)

screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set the resolution

screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic('iss_map.gif')

screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))

iss.penup()
iss.goto(lon, lat)
## turtle.mainloop()

## My Location
yellowlat = 40.5723
yellowlon = -74.6848
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)
mylocation.hideturtle()

passiss = 'http://api.open-notify.org/iss-pass.json'
passiss = passiss + '?lat=' + str(yellowlat) + '&lon=' + str(yellowlon)
response = urllib.request.urlopen(passiss)
result = json.loads(response.read().decode('utf-8'))
# print(result) ## uncomment to see the downloaded result.

over = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
mylocation.write(time.ctime(over), font=style)

turtle.mainloop()
