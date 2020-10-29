#Jake Lorah
#Coded in: Python 3.4.3
#Project2.py

#Updated changes 10/30/18:
   #I changed the name of the methods from forward, backward, left, right, to jakeforward, jakebackward, jakeleft, jakeright.
   #I changed the if condition from < (less than) sign to <= (less than or equal to) sign.
   #I added a new method from the API list called color. turtle.color("black", "darkgreen") changed the color of the turtle to dark green with a black outline.
   #I changed the size of the turtle to make it a little bigger.
   #I changed penup to pendown so that the turtle's path keeps a trail.
   #I changed the background color to dark khaki so that it looks similar to dirty water like a stream or a pond.
   #I added a new method from the API list called stamp that prints the turtle on the screen right when you start the program to show where you began as you move the turtle around the world.
   #I added a second turtle you can control with the keys: W, A, S, D.
   #I changed the dimensions of the screen to be larger.
   #I made the color of turtle2 blue with a white outline.
   #I changed the speed of both turtles to be a little faster.


import turtle

#I changed the dimensions of the screen to be larger and more wide.
HEIGHT = 900
WIDTH = 1200
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)

#Click the image icon in the top right of the code window to see
#which images are available in this trinket

#add the shape first then set the turtle shape

turtle.shape('turtle')

#I made the size of the turtle larger
turtle.shapesize(2)

#I made the color of the turtle dark green with a black outline.
turtle.color("black", "darkgreen")

#Prints the turtle on the screen right when you start the program to show where you began as you move the turtle around the world.
turtle.stamp()

#I changed the background color to dark khaki.
screen.bgcolor("darkkhaki")

#I added the clone method which clones the original turtle.
turtle2 = turtle.clone()

#I made the color of turtle2 blue with a white outline.
turtle2.color("white", "blue")

#I changed the speed of both turtles to be a little faster.
move_speed = 20
turn_speed = 20

#these defs control the movement of our "turtle"

#Changed the name of my method to jakeforward.
def jakeforward():
    turtle.forward(move_speed)
    x, y = turtle.position()

    #Changed the if condition from < (less than) sign to <= (less than or equal to) sign. 
    if not -WIDTH / 2 <= x <= WIDTH / 2 or not -HEIGHT / 2 <= y < HEIGHT / 2:
        turtle.undo() # undo error
        turtle.left(180) # turn around
        turtle.forward(10) # redo movement but in new direction
        
#Changed the name of my method to jakebackward.
def jakebackward():
    turtle.backward(move_speed)
    x, y = turtle.position()
    
#Changed the if condition from < (less than) sign to <= (less than or equal to) sign.
    if not -WIDTH / 2 <= x <= WIDTH / 2 or not -HEIGHT / 2 <= y < HEIGHT / 2:
        turtle.undo() # undo error
        turtle.left(180) # turn around
        turtle.forward(10) # redo movement but in new direction

#Changed the name of my method to jakeleft.
def jakeleft():
    turtle.left(turn_speed)

#Changed the name of my method to jakeright.
def jakeright():
    turtle.right(turn_speed)


#Changed the name of my method to jakeforward2.
def jakeforward2():
    turtle2.forward(move_speed)
    x, y = turtle2.position()

    #Changed the if condition from < (less than) sign to <= (less than or equal to) sign. 
    if not -WIDTH / 2 <= x <= WIDTH / 2 or not -HEIGHT / 2 <= y < HEIGHT / 2:
        turtle2.undo() # undo error
        turtle2.left(180) # turn around
        turtle2.forward(10) # redo movement but in new direction
        
#Changed the name of my method to jakebackward2.
def jakebackward2():
    turtle2.backward(move_speed)
    x, y = turtle2.position()
    
#Changed the if condition from < (less than) sign to <= (less than or equal to) sign.
    if not -WIDTH / 2 <= x <= WIDTH / 2 or not -HEIGHT / 2 <= y < HEIGHT / 2:
        turtle2.undo() # undo error
        turtle2.left(180) # turn around
        turtle2.forward(10) # redo movement but in new direction

#Changed the name of my method to jakeleft2.
def jakeleft2():
    turtle2.left(turn_speed)

#Changed the name of my method to jakeright2.
def jakeright2():
    turtle2.right(turn_speed)

#Changed penup to pendown so that the turtle's path keeps a trail.
turtle.pendown()
turtle.speed(0)
turtle.home()

#Changed penup to pendown so that the turtle 2 path keeps a trail.
turtle2.pendown()
turtle2.speed(0)
turtle2.home()

#now associate the defs from above with certain keyboard events
screen.onkeypress(jakeforward, "Up")

screen.onkeypress(jakebackward, "Down")
screen.onkeypress(jakeleft, "Left")
screen.onkeypress(jakeright, "Right")

screen.onkeypress(jakeforward2, "w")

screen.onkeypress(jakebackward2, "s")
screen.onkeypress(jakeleft2, "a")
screen.onkeypress(jakeright2, "d")
screen.listen()
