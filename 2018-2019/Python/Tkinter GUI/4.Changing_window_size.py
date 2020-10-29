#Name: Jake Lorah
#Date: 11/19/2018
#Program Number: 4.Changing_window_size
#Program Description: This program changes the window size.

from tkinter import *
window = Tk()
window.title("Welcome To Computer Science 4")
window.geometry('1100x500')
addtext= Label(window, text="Hello How are you today", font=("Arial Bold", 70))
addtext.grid(column=0, row=0)
window.mainloop()
