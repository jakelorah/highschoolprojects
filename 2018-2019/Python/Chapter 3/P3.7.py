#Name: Jake Lorah
#Date: 09/27/2018
#Program Number: P3.7.py
#Program Description: This program reads three numbers and prints either increasing, decreasing, or neither depending on what numbers they are.

userInput = input("Please enter your first number: ")
userInput2 = input("Please enter your second number: ")
userInput3 = input("Please enter your third number: ")

if userInput < userInput2 <= userInput3 :
 print ("In order")

 
if userInput > userInput2 >= userInput3 :
 print ("In order")

else :
 print ("Not in order")
