#Name: Jake Lorah
#Date: 11/29/2018
#Program Number: 8. Adding Date Input
#Program Description: This program adds a date input.

from tkinter import *
from time import strptime, strftime
from tkinter.messagebox import showinfo

root = Tk()

def compute():
 global dateEnt
 date = dateEnt.get()
 weekday = strftime('%A', strptime(date, '%b %d, %Y'))
 showinfo(message = '{} was a {}'.format(date, weekday))
 dateEnt.delete(0, END)
 
label = Label(root, text='Enter Date')
label.grid(row=0, column=0)

dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)

button= Button(root, text='Enter', command=compute)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()
