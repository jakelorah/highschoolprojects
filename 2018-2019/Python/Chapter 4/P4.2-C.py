#Name: Jake Lorah
#Date: 10/10/2018
#Program Number: P4.2-C.py
#Program Description: This program finds the cumulative totals.

total = 0
inputStr2 = input("Enter a value: ")
while inputStr2 != "" :
    value2 = int(inputStr2)
    total = total + value2
    print(total)
    inputStr2 = input("Enter another value: ")
