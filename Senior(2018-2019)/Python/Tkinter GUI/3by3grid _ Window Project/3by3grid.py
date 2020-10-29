#Name: Jake Lorah
#Date: 11/26/2018
#Program Number: 3by3grid
#Program Description: This program adds a 3 by 3 grid and adds something in each box.

from tkinter import *
 
window = Tk()
 
window.title("3 x 3 Grid Lab - Jake Lorah")

window.geometry('1100x600')

first= Label(window, text="     PCTI1     ", font=("Arial Bold", 50))
second= Label(window, text="    PCTI2     ", font=("Arial Bold", 50))
third= Label(window, text="     PCTI3    ", font=("Arial Bold", 50))

first.grid(column=0, row=0)
second.grid(column=1, row=0)
third.grid(column=2, row=0)

def windowsize():
    window.geometry('1150x600')
    fourth.configure(text="Window size changed!!")

def textsize():
    first.config(font=("Courier", 30))
    second.config(font=("Courier", 30))
    third.config(font=("Courier", 30))
    fifth.configure(text="Text size and font changed!!")

def color():
    first.config(fg="red")
    second.config(fg="red")
    third.config(fg="red")
    sixth.configure(text="Text color changed!!")

def default():
    window.geometry('1100x600')
    first.config(font=("Arial Bold", 50))
    second.config(font=("Arial Bold", 50))
    third.config(font=("Arial Bold", 50))
    first.config(fg="black")
    second.config(fg="black")
    third.config(fg="black")
    tenth.configure(text="Back to the start!")
    
fourth= Button(window, text="Click to change window size", command=windowsize)
fifth= Button(window, text="Click to change text size and font", command=textsize)
sixth= Button(window, text="Click to change text color", command=color)

fourth.grid(column=0, row=1)
fifth.grid(column=1, row=1)
sixth.grid(column=2, row=1)

photo1 = PhotoImage(file="pic1.gif")
photo2 = PhotoImage(file="pic2.gif")
photo3 = PhotoImage(file="pic3.gif")

seventh= Label(window, image = photo1)
eighth= Label(window, image = photo2)
ninth= Label(window, image = photo3)

seventh.grid(column=0, row=2)
eighth.grid(column=1, row=2)
ninth.grid(column=2, row=2)

tenth= Button(window, text="Click to go back to the default state", command=default)
tenth.grid(column=1, row=5)


window.mainloop()

