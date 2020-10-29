#Name: Jake Lorah
#Date: 10/10/2018
#Program Number: P4.2-Max.py
#Program Description: This program finds the max.

#A - Maximum
largest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "" :
    value = int(inputStr)
    if value > largest :
        largest = value
    inputStr = input("Enter another value: ")
print ("The maximum is", value)
