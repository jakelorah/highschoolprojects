#Name: Jake Lorah
#Date: 09/26/2018
#Program Number: P3.4.py
#Program Description: This program reads three numbers and prints either all the same, all different, or neither depending on what numbers they are.

userInput = input("Please enter your first number: ")
userInput2 = input("Please enter your second number: ")
userInput3 = input("Please enter your third number: ")

if userInput == userInput2 == userInput3 :
 print ("All the same")

 
if userInput != userInput2 != userInput3 :
 print ("All different")

else :
    print("Neither")
