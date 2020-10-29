#Jake Lorah
#Coded in: Python 3.4.3
#Uses turtle graphics to create an abstract design

import turtle

aScreen = turtle.Screen()
shelly = turtle.Turtle()

shelly.color('orange', 'blue')

shelly.begin_fill()

shelly.width(7)

shelly.speed(20)

a = 0
b = 150
c = 200

for i in range (0,1):
    shelly.forward(1000 * i)
    shelly.circle(250 + i)
    shelly.forward(1000 * i)
    shelly.circle(220 + i)
    shelly.forward(1000 * i)
    shelly.circle(190 + i)
    shelly.forward(1000 * i)
    shelly.circle(160 + i)
    shelly.forward(1000 * i)
    shelly.circle(130 + i)
    shelly.forward(1000 * i)
    shelly.circle(100 + i)
    shelly.forward(1000 * i)
    shelly.circle(70 + i)
    shelly.forward(1000 * i)
    shelly.circle(40 + i)
    shelly.forward(1000 * i)
    shelly.circle(10 + i)
    shelly.forward(1000 * i)
    shelly.circle(0 + i)

    shelly.end_fill()

for i in range (0,1):
   shelly.color('lightblue')
   shelly.penup()
   shelly.bk(500)
   shelly.left(100)
   shelly.bk(50)
   shelly.right(100)
   shelly.pendown()
   shelly.forward(950)
   
