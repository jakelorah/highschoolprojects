#Name: Jake Lorah
#Date: 12/13/2018
#Program Number: Final_Project
#Program Description: This program is the final project for tkinter. It is calculating user input and printing an invoice.

from tkinter import *

import tkinter as tk
 
window = Tk()
root = Tk()
window.title("Final Project - Jake Lorah")
window.geometry('1000x500')

firsttitle = Label(window, text="Fidget Spinner Order Form", font=("Arial Bold", 20))
firsttitle.place(x=0,y=0)

fullname= Label(window, text="Full Name: ", font=("Times New Roman", 15))
fullname.place(x=0,y=80)

global fullnameentry
fullnameentry = Entry(window, width=25)
fullnameentry.place(x=105,y=86)

global address
address= Label(window, text="Address: ", font=("Times New Roman", 15))
address.place(x=0,y=130)

addressentry = Entry(window, width=25)
addressentry.place(x=105,y=135)

modeltype= Label(window, text="Model Types: ", font=("Times New Roman", 15))
modeltype.place(x=0,y=179)

buttons = IntVar()
global basicitem
basicitem= Radiobutton(window, text="Basic", value = 1, variable = buttons, font=("Times New Roman", 15))
basicitem.place(x=125,y=177)

global deluxeitem
deluxeitem= Radiobutton(window, text="Deluxe", value = 2, variable = buttons, font=("Times New Roman", 15))
deluxeitem.place(x=125,y=215)

global premiumitem
premiumitem= Radiobutton(window, text="Premium", value = 3, variable = buttons, font=("Times New Roman", 15))
premiumitem.place(x=125,y=253)

units= Label(window, text="# of units: ", font=("Times New Roman", 15))
units.place(x=0,y=303)

unitsentry = Entry(window, width=5)
unitsentry.place(x=105,y=309)

discountcode= Label(window, text="Discount Code: ", font=("Times New Roman", 15))
discountcode.place(x=0,y=353)

discountcodeentry = Entry(window, width=15)
discountcodeentry.place(x=145,y=358)

pricingtitle= Label(window, text="Pricing", font=("Times New Roman", 15))
pricingtitle.place(x=700,y=53)

pricingbasictitle= Label(window, text="Basic: ", font=("Times New Roman", 15))
pricingbasictitle.place(x=600,y=100)

pricingbasic= Label(window, text="1-10 Units: $5", font=("Times New Roman", 15))
pricingbasic.place(x=675,y=100)

pricingbasic2= Label(window, text=">10 Units units: $3", font=("Times New Roman", 15))
pricingbasic2.place(x=675,y=140)

pricingdeluxetitle= Label(window, text="Deluxe: ", font=("Times New Roman", 15))
pricingdeluxetitle.place(x=593,y=210)

pricingdeluxe= Label(window, text="1-10 Units: $10", font=("Times New Roman", 15))
pricingdeluxe.place(x=675,y=210)

pricingdeluxe2= Label(window, text=">10 Units units: $6", font=("Times New Roman", 15))
pricingdeluxe2.place(x=675,y=250)

pricingpremiumtitle= Label(window, text="Premium: ", font=("Times New Roman", 15))
pricingpremiumtitle.place(x=581,y=320)

pricingpremium= Label(window, text="1-10 Units: $15", font=("Times New Roman", 15))
pricingpremium.place(x=675,y=320)

pricingpremium2= Label(window, text=">10 Units units: $9", font=("Times New Roman", 15))
pricingpremium2.place(x=675,y=360)
    
def new_winF(): 
    newwin = Toplevel(window)
    newwin.geometry('1000x500')
    title = Label(newwin, text="Invoice",font=("Times New Roman", 25))
    title.place(x=450,y=0)
    
    FullName = Label(newwin, text="Full Name",font=("Verdana 10 bold", 17))
    FullName.place(x=1,y=60)
    firstname2 = fullnameentry.get()
    FullName3 = Label(newwin, text=firstname2,font=("Times New Roman", 15))
    FullName3.place(x=1,y=95)
    
    FullName4 = Label(newwin, text="Address",font=("Verdana 10 bold", 17))
    FullName4.place(x=4,y=140)
    address2 = addressentry.get()
    Theaddress3 = Label(newwin, text=address2,font=("Times New Roman", 15))
    Theaddress3.place(x=1,y=175)

    FullName5 = Label(newwin, text="Model Type",font=("Verdana 10 bold", 17))
    FullName5.place(x=1,y=220)
    value = buttons.get()
    price = 0
    if value == 1 :
        FullName6 = Label(newwin, text="Basic",font=("Times New Roman", 15))
        FullName6.place(x=1,y=255)
        if int(unitsentry.get()) >= 1 and int(unitsentry.get()) <= 10 :
            price = 5 * int(unitsentry.get())
        if int(unitsentry.get()) > 10 :
            price = 3 * int(unitsentry.get())
            
    if value == 2 :
        FullName7 = Label(newwin, text="Deluxe",font=("Times New Roman", 15))
        FullName7.place(x=1,y=255)
        if int(unitsentry.get()) >= 1 and int(unitsentry.get()) <= 10 :
            price = 10 * int(unitsentry.get())
        if int(unitsentry.get()) > 10 :
            price = 6 * int(unitsentry.get())
    if value == 3 :
        FullName8 = Label(newwin, text="Premium",font=("Times New Roman", 15))
        FullName8.place(x=1,y=255)
        if int(unitsentry.get()) >= 1 and int(unitsentry.get()) <= 10 :
            price = 15 * int(unitsentry.get())
        if int(unitsentry.get()) > 10 :
            price = 9 * int(unitsentry.get())

    FullName10 = Label(newwin, text="# of Units",font=("Verdana 10 bold", 17))
    FullName10.place(x=4,y=300)
    address11 = unitsentry.get()
    Theaddress12 = Label(newwin, text=address11,font=("Times New Roman", 15))
    Theaddress12.place(x=1,y=335)


    if discountcodeentry.get() == "HOLIDAY20" :
     FullName15 = Label(newwin, text="Discount Code Applied",font=("Times New Roman Bold", 15))
     FullName15.place(x=1,y=375)
     discount = price * 0.2
     total = price - discount
     stringify = str(total)
     FullName35 = Label(newwin, text="Total: $" + stringify + "0",font=("Times New Roman Bold", 20))
     FullName35.place(x=2,y=430)
    else :
     stringify = str(price)
     FullName35 = Label(newwin, text="Total: $" + stringify,font=("Times New Roman Bold", 20))
     FullName35.place(x=3,y=430)

         
    
def default():
  fullnameentry.delete(0, END)
  fullnameentry.insert(0, "")
  addressentry.delete(0, END)
  addressentry.insert(0, "")
  basicitem.deselect()
  deluxeitem.deselect()
  premiumitem.deselect()
  unitsentry.delete(0, END)
  unitsentry.insert(0, "")
  discountcodeentry.delete(0, END)
  discountcodeentry.insert(0, "")
  
addbutton = Button(window, text="Calculate", bg="#d3e4ff", fg="black", command=new_winF)

addbutton.place(x=150,y=420)

addbutton2 = Button(window, text="Clear", bg="black", fg="white", command=default)

addbutton2.place(x=40,y=420)


window.mainloop()
root.mainloop()
