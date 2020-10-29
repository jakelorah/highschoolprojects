#Name: Jake Lorah
#Date: 10/11/2018
#Program Number: P4.2-D.py
#Program Description: This program finds all adjacent duplicates.

total = 0
total2 = 0
inputStr = input("Enter a value: ")
inputStr2 = input("Enter a value: ")
while inputStr != "" :
    value2 = int(inputStr)
    inputStr2 = int(inputStr2)

    if value2 == inputStr2 :
        print("It is a duplicate")
        total = value2
        print(total)
        total2 = total2 + 1
        inputStr = input("Enter a value: ")
        inputStr2 = input("Enter a value: ")
        
print(total2)
 
