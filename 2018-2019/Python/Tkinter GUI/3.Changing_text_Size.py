#Name: Jake Lorah
#Date: 11/19/2018
#Program Number: 3.Changing_text_Size
#Program Description: This program changes text size.

from tkinter import *
window = Tk()
window.title("Welcome To Computer Science 4")
addtext= Label(window, text="Hello How are you today", font=("Arial Bold", 70))
addtext.grid(column=0, row=0)
window.mainloop()
