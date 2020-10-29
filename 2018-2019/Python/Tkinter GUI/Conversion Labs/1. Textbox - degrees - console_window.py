#Name: Jake Lorah
#Date: 12/7/2018
#Program Number: 1. Textbox - degrees - console_window
#Program Description: This program converts Fahrenheit to Celsius and prints it in console window.

from tkinter import *
 
window = Tk()
window.title("Welcome To Computer Science 4")
window.geometry('350x200')

addtext= Label(window, text="Enter the temperature in Celsius: ")
addtext.grid(column=0, row=0)

c = Entry(window)
c.insert(10, "")
c.grid(column = 1, row = 0)

def retrieve_input():
    convertCel = 0
    cel = int(c.get())
    convertCel = cel * 1.8 + 32
    print(convertCel, "°F")


def default():
  c.delete(0, END)
  c.insert(0, "")

addbutton2 = Button(window, text="Reset", bg="black", fg="red", command=default)

addbutton2.grid(column=0, row=5)


addbutton = Button(window, text="Convert", bg="black", fg="red", command=retrieve_input)

addbutton.grid(column=0, row=4) 


window.mainloop()
