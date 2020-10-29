#Name: Jake Lorah
#Date: 12/11/2018
#Program Number: 12.Random_Number
#Program Description: This program asks the user to guess a random number.

import random

user = int(input("Guess the number from 1-10: "))
x = random.randint(1, 10) 
if user < x :
   print("Too low. Please try again.")
if user > x :
   print("Too high. Please try again.")
if user == x : 
   print("Correct! You got it.")

while user != ("") :
 user = int(input("Guess the number from 1-10: "))
 
 
 if user < x :
   print("Too low. Please try again.")
 if user > x :
   print("Too high. Please try again.")
 if user == x : 
   print("Correct! You got it.")
