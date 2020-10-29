#Name: Jake Lorah
#Date: 12/5/2018
#Program Number: 11.Radio_button
#Program Description: This program adds a radio button.

from tkinter import *

from tkinter.ttk import *

FormWindow = Tk()
 
FormWindow.title("Welcome To Computer Science 4")

FormWindow.geometry('350x200')
var = IntVar()
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   print(selection)
   return selection

RadioButtonQuestionOne= Label(FormWindow, text= "How much do you like this CS4:", font=("Arial Bold", 17), background="White").grid(sticky=W)

radbutton1 = Radiobutton(FormWindow, text='Strongly Dislike', variable=var, value=1,command=sel).grid(sticky=W)
radbutton2 = Radiobutton(FormWindow, text='Dislike',variable=var, value=2,command=sel).grid(sticky=W)
radbutton3 = Radiobutton(FormWindow, text='Like', variable=var, value=3,command=sel).grid(sticky=W)
radbutton4 = Radiobutton(FormWindow, text='Strongly Like', variable=var, value=4,command=sel).grid(sticky=W)
label = Label(FormWindow)
FormWindow.mainloop()
