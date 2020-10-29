#Jake Lorah
#Coded in: Python 3.4.3
#Uses turtle Graphics to create square

import turtle

aScreen = turtle.Screen()
shelly = turtle.Turtle()

#Change color to orange and blue
shelly.color('orange', 'blue')

shelly.begin_fill()

#Make the thickness larger by 7
shelly.width(7)

#Make all forward numbers 200 instead of 100
shelly.forward(200)

shelly.left(270)

shelly.forward(200)

shelly.left(270)

shelly.forward(200)

shelly.left(270)

shelly.forward(200)

shelly.end_fill()
