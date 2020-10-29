#Name: Jake Lorah
#Date: 12/5/2018
#Program Number: 10.Check_box
#Program Description: This program adds a check box.

from tkinter import *

from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome To Computer Science 4")



window.geometry('350x200')
var = IntVar()
def sel():
   selection = "You selected the option 1" 
   print(selection)
   return selection

def sel2():
   selection = "You selecteselectedd the option 2" 
   print(selection)
   return selection

def sel3():
   selection = "You selected the option 3" 
   print(selection)
   return selection

def sel4():
   selection = "You selected the option 4" 
   print(selection)
   return selection

def sel5():
   selection = "You selected the option 5" 
   print(selection)
   return selection



chk = Checkbutton(window, text='Option 1', command=sel)

chk1 = Checkbutton(window, text='Option 2', command=sel2)

chk2 = Checkbutton(window, text='Option 3', command=sel3)

chk3 = Checkbutton(window, text='Option 4', command=sel4)

chk4 = Checkbutton(window, text='Option 5', command=sel5)

chk.grid(column=0, row=0)

chk1.grid(column=0, row=1)

chk2.grid(column=0, row=2)

chk3.grid(column=0, row=3)

chk4.grid(column=0, row=4)

label = Label(window)


window.mainloop()
