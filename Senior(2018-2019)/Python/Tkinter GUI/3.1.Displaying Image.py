#Name: Jake Lorah
#Date: 11/20/2018
#Program Number: 3.1.Displaying Image
#Program Description: This program displays an image, along with other brag points.


#Baseline Code
from tkinter import *
 
window = Tk()
 
window.title("Display Image")

photo = PhotoImage(file='peace.gif')

#Changed the size of the window to be larger
peace = Label(master= window, image= photo, width = 700, height= 400)

peace.pack()

#Changed the text, text font, and text size.
addtext= Label(window, text="Live Life Peacefully", font=("Times New Roman", 50))

addtext.pack(side=BOTTOM)

from tkinter import *
import webbrowser

def callback(event):
    webbrowser.open_new(r"https://en.wikipedia.org/wiki/Peace")


root = Tk()
link = Label(root, text="Click here to go to the Peace Website", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)
root.mainloop()

window = Tk()
print("Are you sure you want to leave?")
b = Button(window, text="Yes", command=window.destroy)
b.pack()

c = Button(window, text="No")
c.pack()

mainloop()

window.mainloop()
