#Name: Jake Lorah
#Date: 12/13/2018
#Program Number: Final_Project
#Program Description: This program is the final project for tkinter. It is calculating user input and printing an invoice.

from tkinter import *

import tkinter as tk

import os
 
window = Tk()

window.title("Survey Form - Jake Lorah")
window.geometry('1000x500')

firsttitle = Label(window, text="Survey Form", font=("Arial Bold", 20))
firsttitle.place(x=0,y=0)

fullname= Label(window, text="Full Name: ", font=("Times New Roman", 15))
fullname.place(x=0,y=80)

global fullnameentry
fullnameentry = Entry(window, width=25)
fullnameentry.place(x=105,y=86)

firsttitle5 = Label(window, text="Do you enjoy Computer Science?", font=("Times New Roman", 15))
firsttitle5.place(x=0,y=150)

buttons = IntVar()
global basicitem
basicitem= Radiobutton(window, text="Yes", value = 1, variable = buttons, font=("Times New Roman", 15))
basicitem.place(x=280,y=150)

global deluxeitem
deluxeitem= Radiobutton(window, text="No", value = 2, variable = buttons, font=("Times New Roman", 15))
deluxeitem.place(x=280,y=180)

firsttitle7 = Label(window, text="Which section is your favorite?", font=("Times New Roman", 15))
firsttitle7.place(x=0,y=260)

buttons3 = IntVar()
buttons4 = IntVar()
buttons5 = IntVar()

basicitem2= Checkbutton(window, text="Basic Python", variable = buttons3, font=("Times New Roman", 15))
basicitem2.place(x=280,y=260)


deluxeitem3= Checkbutton(window, text="Tkinter", variable = buttons4, font=("Times New Roman", 15))
deluxeitem3.place(x=280,y=290)


deluxeitem4= Checkbutton(window, text="Turtle Graphics", variable = buttons5, font=("Times New Roman", 15))
deluxeitem4.place(x=280,y=320)


def new_winF():
    newwin = Toplevel(window)
    newwin.geometry('1000x500')
    title = Label(newwin, text="Please check your information",font=("Times New Roman", 25))
    title.place(x=320,y=0)
    
    FullName = Label(newwin, text="Full Name",font=("Verdana 10 bold", 17))
    FullName.place(x=1,y=60)
    firstname2 = fullnameentry.get()
    FullName3 = Label(newwin, text=firstname2,font=("Times New Roman", 15))
    FullName3.place(x=1,y=95)
    

    FullName5 = Label(newwin, text="Do you enjoy Computer Science?",font=("Verdana 10 bold", 17))
    FullName5.place(x=1,y=160)
    if buttons.get() == 1 :
     FullName30 = Label(newwin, text="Yes",font=("Times New Roman", 15))
     FullName30.place(x=1,y=200)
    if buttons.get() == 2 :
     FullName30 = Label(newwin, text="No",font=("Times New Roman", 15))
     FullName30.place(x=1,y=200)

    FullName50 = Label(newwin, text="Which section is your favorite?",font=("Verdana 10 bold", 17))
    FullName50.place(x=1,y=265)
    if buttons3.get() == 1 :
     FullName300 = Label(newwin, text="Basic Python",font=("Times New Roman", 15))
     FullName300.place(x=1,y=305)
    if buttons4.get() == 1 :
     FullName300 = Label(newwin, text="Tkinter",font=("Times New Roman", 15))
     FullName300.place(x=1,y=335)
    if buttons5.get() == 1 :
     FullName300 = Label(newwin, text="Turtle Graphics",font=("Times New Roman", 15))
     FullName300.place(x=1,y=365)
    def close_window(): 
     window.destroy()
     newwin.destroy()

    def goback() :
        global newwin
        newwin.destroy()
        os.system("Survey-Form.py")

    addbutton23 = Button(newwin, text="Go back", bg="#680912", fg="WHITE", command=goback)

    

    addbutton24 = Button(newwin, text="Final Submission", bg="#084212", fg="white", command=close_window)

    addbutton24.place(x=100,y=440)
    
def default():
  fullnameentry.delete(0, END)
  fullnameentry.insert(0, "")
  basicitem.deselect()
  deluxeitem.deselect()
  basicitem2.deselect()
  deluxeitem3.deselect()
  deluxeitem4.deselect()
  
addbutton = Button(window, text="Submit", bg="#d3e4ff", fg="black", command=new_winF)

addbutton.place(x=150,y=420)

addbutton2 = Button(window, text="Clear", bg="black", fg="white", command=default)

addbutton2.place(x=40,y=420)


window.mainloop()

