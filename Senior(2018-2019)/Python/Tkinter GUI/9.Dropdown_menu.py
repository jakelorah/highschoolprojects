#Name: Jake Lorah
#Date: 12/5/2018
#Program Number: 9.Dropdown_menu
#Program Description: This program adds a dropdown menu.

from tkinter import *
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome To Computer Science 4")

window.geometry('1100x500') 

dropdown = Combobox(window)

dropdown['values']=(1,2,3,4,5,"Text")

dropdown.current(0)#set the selected item

dropdown.grid(column=0, row=0)

window.mainloop()
