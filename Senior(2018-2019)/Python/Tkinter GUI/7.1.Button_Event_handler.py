#Name: Jake Lorah
#Date: 11/26/2018
#Program Number: 7.1.Button_Event_handler
#Program Description: This program adds a button event handler.

from tkinter import *
from time import strftime, localtime

def clicked():
    'prints day and time info'
    time = strftime('Day: %d %b %y \nTime: %H:%M:%S %p\n', localtime())
    print(time)


root = Tk()
 
root.title("Time and Date")

root.geometry('700x700')

button = Button(root, text="Click me", command=clicked)

button.pack()
 
root.mainloop()
