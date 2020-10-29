#Name: Jake Lorah
#Date: 11/29/2018
#Program Number: 8.1 Adding Textbox
#Program Description: This program adds a textbox.

from tkinter import *

root=Tk()

def retrieve_input():
 inputValue=textBox.get("1.0","end-1c")
 print(inputValue)
 
textBox=Text(root, height=2, width=10)
textBox.pack()

buttonCommit=Button(root, height=1, width=10, text="Commit",command=lambda: retrieve_input())
buttonCommit.pack()

mainloop()
