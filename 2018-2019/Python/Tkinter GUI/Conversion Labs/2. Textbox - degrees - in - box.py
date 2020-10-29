#Name: Jake Lorah
#Date: 12/7/2018
#Program Number: 2. Textbox - degrees - in - box
#Program Description: This program converts Fahrenheit to Celsius and prints it in window.

from tkinter import *

import os
 
window = Tk()
window.title("Welcome To Computer Science 4")
window.geometry('350x200')

addtext= Label(window, text="Enter the temperature in Celsius: ")
addtext.grid(column=0, row=0)

addtext2= Label(window, text="Temperature in Fahrenheit: ")
addtext2.grid(column=0, row=1)

c = Entry(window)

c.grid(column = 1, row = 0)

f = Entry(window)

f.grid(column = 1, row = 1)

def retrieve_input():
    convertCel = 0
    cel = int(c.get())
    convertCel = cel * 1.8 + 32
    stringify = str(convertCel)
    f.insert(10,stringify + "°F")

def default():
  c.delete(0, END)
  c.insert(0, "")
  f.delete(0, END)
  f.insert(0, "")

addbutton = Button(window, text="Convert", bg="black", fg="red", command=retrieve_input)

addbutton.grid(column=0, row=4)

addbutton2 = Button(window, text="Reset", bg="black", fg="red", command=default)

addbutton2.grid(column=0, row=5)


window.mainloop()
