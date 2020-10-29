#Jake Lorah
#Coded in: Python 3.4.3
#Uses turtle graphics to create a circle

import turtle

aScreen = turtle.Screen()
shelly = turtle.Turtle()

#Change color to orange and blue
shelly.color('orange', 'blue')

shelly.begin_fill()

#Make the thickness larger by 7
shelly.width(7)

#Make all forward numbers 200 instead of 100
shelly.forward(12)

#Create a circle instead of a square
shelly.circle(100)

shelly.end_fill()
