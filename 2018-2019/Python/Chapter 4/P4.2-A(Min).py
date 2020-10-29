#Name: Jake Lorah
#Date: 10/10/2018
#Program Number: P4.2-Min.py
#Program Description: This program finds the min.

#A - Minimum
smallest = 10000
largest = 0
largest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "" :
    value = int(inputStr)
    if value < largest :
        largest = value
    inputStr = input("Enter another value: ")
print ("The minimum is", largest)
