#Name: Jake Lorah
#Date: 12/11/2018
#Program Number: 12.Random_Number_Tkinter
#Program Description: This program asks the user to guess a random number in tkinter.

from tkinter import *

import os

import random
 
window = Tk()
window.title("Randon Number Game - Jake Lorah")
window.geometry('350x200')

user= Label(window, text="Guess the number from 1-10: ")
user.grid(column=0, row=0)

addtext2= Label(window, text="Answer: ")
addtext2.grid(column=0, row=1)

c = Entry(window)

c.grid(column = 1, row = 0)

f = Entry(window)

f.grid(column = 1, row = 1)

randomnumber = random.randint(0, 10)

def retrieve_input():
   global number
   global r
   number = float(c.get())

   if number > randomnumber :
     f.insert(0, "Too high")

   elif number < randomnumber :
     f.insert(0, "Too low")
      
   elif number == randomnumber :
     f.insert(0, "Correct")

def default():
  c.delete(0, END)
  c.insert(0, "")
  f.delete(0, END)
  f.insert(0, "")

addbutton = Button(window, text="Check!", bg="black", fg="red", command=retrieve_input)

addbutton.grid(column=0, row=4)

addbutton2 = Button(window, text="Reset", bg="black", fg="red", command=default)

addbutton2.grid(column=0, row=5)


window.mainloop()

