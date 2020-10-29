#Name: Jake Lorah
#Date: 12/3/2018
#Program Number: 10-buttons
#Program Description: This program adds 10 different buttons to the window, all performing different actions.

from tkinter import *
 
window = Tk()
 
window.title("10-buttons Lab - Jake Lorah")

window.geometry('1100x600')

zero= Label(window, text="     10-buttons Lab - Jake Lorah    ", font=("Arial Bold", 30),fg="#084b72")

def bgcolor():
   window.configure(background='#afdbd3')
   first.configure(text="Background color changed")
   
def textcolorandsize():
    first.config(font=("Arial Bold", 15),fg="#9356a5")
    second.config(font=("Arial Bold", 15),fg="#9356a5")
    third.config(font=("Arial Bold", 15),fg="#9356a5")
    fourth.config(font=("Arial Bold", 15),fg="#9356a5")
    fifth.config(font=("Arial Bold", 15),fg="#9356a5")
    sixth.config(font=("Arial Bold", 15),fg="#9356a5")
    seventh.config(font=("Arial Bold", 15),fg="#9356a5")
    eighth.config(font=("Arial Bold", 15),fg="#9356a5")
    ninth.config(font=("Arial Bold", 15),fg="#9356a5")
    tenth.config(font=("Arial Bold",15),fg="#9356a5")
    second.config(text="Text color and size changed")

def windowsize():
    window.geometry('1400x800')
    fourth.configure(text="Window size changed")

    
first= Button(window, text="     Click to change the bg color     ",command=bgcolor, font=("Arial Bold", 10))
second= Button(window, text="    Click to change the text color and size     ",command=textcolorandsize, font=("Arial Bold", 10))
third= Button(window, text="     Click to change the window size    ",command=windowsize, font=("Arial Bold", 10))

zero.grid(column=0, row=0)
first.grid(column=0, row=3)
second.grid(column=0, row=4)
third.grid(column=0, row=5)

def image():
 

    
fourth= Button(window, text="    Click to display an image      ",command=image, font=("Arial Bold", 10))
fifth= Button(window, text="     Click to change an image     ", font=("Arial Bold", 10))
sixth= Button(window, text="     Click to play a sound     ", font=("Arial Bold", 10))

fourth.grid(column=0, row=6)
fifth.grid(column=0, row=7)
sixth.grid(column=0, row=8)

seventh=  Button(window, text="    Click to print the date     ", font=("Arial Bold", 10))
eighth=  Button(window, text="    Click to open a web page     ", font=("Arial Bold", 10))
ninth= Button(window, text="    Click to open a new window and then go back to the previous window     ", font=("Arial Bold", 10))

seventh.grid(column=0, row=9)
eighth.grid(column=0, row=10)
ninth.grid(column=0, row=11)

tenth=  Button(window, text="     Click to open a game (turtle racing) with filename     ", font=("Arial Bold", 10))

tenth.grid(column=0, row=12)


window.mainloop()

