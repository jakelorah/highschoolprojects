#Name: Jake Lorah
#Date: 11/26/2018
#Program Number: 7.Button_Event_handler
#Program Description: This program adds a button event handler.

from tkinter import *
 
window = Tk()
 
window.title("Welcome To Computer Science 4")

window.geometry('1100x500')

addtext= Label(window, text="Hello How are you today", font=("Arial Bold", 70))

addtext.grid(column=0, row=0)

count = 0
def clicked():
    global count
    old = '1000x500'
    addtext.configure(text="Button was Clicked!!")
    window.geometry(old)
    count = count + 1
    if count % 2 == 0:
        window.geometry('1100x500')
        addtext.configure(text = "Hello How are you today")

addbutton = Button(window, text="Click me", bg="black", fg="red", command=clicked)

addbutton.grid(column=0, row=2)
 
window.mainloop()
