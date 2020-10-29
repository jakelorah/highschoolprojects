#Name: Jake Lorah
#Date: 11/26/2018
#Program Number: 3by3grid
#Program Description: This program adds a 3 by 3 grid and adds something in each box.

from tkinter import *
 
window = Tk()
 
window.title("3 x 3 Grid Lab - Jake Lorah")

window.geometry('1100x500')

pcti = PhotoImage(file='pic1.gif')
image = label(window, image = pcti, width = 300, height = 700)
image.grid(column=0, row=1)

window.mainloop()

