#Name: Jake Lorah
#Date: 12/4/18
#File Name: jaketest.py
#File Description: This code will change the window size and display image.


from tkinter import *
 
window = Tk()
 
window.title("Jake Test")

window.geometry('1100x600')

pctipic = PhotoImage(file="image.gif")
image2=Label(master=window,image=pctipic)
    
def windowsize():
    window.geometry('1300x800')

windowsize = Button(window, text="Click here to change window size", command=windowsize)
windowsize.pack()

def image1():   
    image2.pack( side = BOTTOM )
    
    
image5 = Button(window, text="Click here to add an image", command=image1)
image5.pack()

   
def default():
    window.geometry('1100x600')

default = Button(window, text="Click here to go back to default", command=default)
default.pack()

 
mainloop()    
