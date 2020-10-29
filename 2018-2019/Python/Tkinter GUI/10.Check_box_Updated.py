#Name: Jake Lorah
#Date: 12/5/2018
#Program Number: 10.Check_box
#Program Description: This program adds a check box.

from tkinter import *

from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome To Computer Science 4")

window.geometry('350x200')

chk_state = BooleanVar()

chk_state.set(True)

count = 0
def function1():

    global count
    count = count + 1
    if count%2 == 1:
        print('You selected option 1')
    else:
        print("You unselected option 1")
        
chk = Checkbutton(window, text='Option 1', command = function1)

def function2():
    global count
    count = count + 1
    if count%2 == 1:
        print('You selected option 2')
    else:
        print("You unselected option 2")
chk1 = Checkbutton(window, text='Option 2', command = function2)

def function3():
    global count
    count = count + 1
    if count%2 == 1:
        print('You selected option 3')
    else:
        print("You unselected option 3")

chk2 = Checkbutton(window, text='Option 3', command = function3)

def function4():
    global count
    count = count + 1
    if count%2 == 1:
        print('You selected option 4')
    else:
        print("You unselected option 4")

chk3 = Checkbutton(window, text='Option 4', command = function4)

def function5():
    global count
    count = count + 1
    if count%2 == 1:
        print('You selected option 5')
    else:
        print("You unselected option 5")

        
chk4 = Checkbutton(window, text='Option 5', command = function5)

chk.grid(column=0, row=0)

chk1.grid(column=0, row=1)

chk2.grid(column=0, row=2)

chk3.grid(column=0, row=3)

chk4.grid(column=0, row=4)

window.mainloop()
