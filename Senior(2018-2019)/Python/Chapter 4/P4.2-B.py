#Name: Jake Lorah
#Date: 10/10/2018
#Program Number: P4.2-B.py
#Program Description: This program finds the number of even and odd inputs.


even = 0
odd = 0
inputStr2 = input("Enter a value: ")
while inputStr2 != "" :
    value2 = int(inputStr2)
    if value2 %2 == 0 :
        even = even + 1
    else :
        odd = odd + 1
    inputStr2 = input("Enter another value: ")
print()
print ("The amount of even numbers is", even)
print()
print ("The amount of odd numbers is", odd)
