#Name: Jake Lorah
#Date: 12/10/2018
#Program Number: 4. Textbox -BMI - in - box
#Program Description: This program finds your BMI from your height and weight.

from tkinter import *

import os
 
window = Tk()
window.title("BMI Calculator")
window.geometry('350x200')

addtext= Label(window, text="Enter height in feet: ")
addtext.grid(column=0, row=2)

addtext2= Label(window, text="Enter weight in pounds: ")
addtext2.grid(column=0, row=3)


addtext3= Label(window, text="BMI: ")
addtext3.grid(column=0, row=4)


feet = Entry(window)

feet.grid(column = 1, row = 2)

pounds = Entry(window)

pounds.grid(column = 1, row = 3)

BMI2 = Entry(window)

BMI2.grid(column = 1, row = 4)

def retrieve_input():
  height = float(feet.get())
  converth = height * 0.3048

  weight = float(pounds.get())
  convertw = weight * 0.453592

  BMI = convertw / converth**2

  stringify = str(BMI)

  BMI2.insert(0, stringify + "BMI")

def default():
  feet.delete(0, END)
  feet.insert(0, "")
  pounds.delete(0, END)
  pounds.insert(0, "")
  BMI2.delete(0, END)
  BMI2.insert(0, "")

addbutton = Button(window, text="Calculate", bg="#d3e4ff", fg="black", command=retrieve_input)

addbutton.grid(column=1, row=5)

addbutton2 = Button(window, text="Reset", bg="black", fg="white", command=default)

addbutton2.grid(column=0, row=5)

title = Label(window, text="BMI Calculation - Jake Lorah", font=("Arial Bold",8))
 
title.grid(column=0, row=0)

title2 = Label(window, text="*Please round numbers.")

title2.grid(column=0, row=1)



window.mainloop()
