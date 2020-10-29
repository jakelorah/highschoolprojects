#Name: Jake Lorah
#Date: 11/26/2018
#Program Number: 8.Adding_text_input
#Program Description: This program adds text input.

from tkinter import *
 
window = Tk()
 
window.title("Welcome To Computer Science 4")

window.geometry('1100x500')

addtext= Label(window, text="Hello How are you today", font=("Arial Bold", 70))

addtext.grid(column=0, row=0)
def clicked():
    addtext.configure(text="Button was Clicked!!")
    window.geometry('1000x500')

addbutton = Button(window, text="Click me", bg="black", fg="red", command=clicked)

addbutton.grid(column=0, row=2) 

Userinput = Entry(window, width=10)

Userinput.grid(column=0, row=3)

Userinput.focus()

window.mainloop()
