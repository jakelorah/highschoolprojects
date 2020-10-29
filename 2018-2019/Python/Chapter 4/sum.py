#Name: Jake Lorah
#Date: 10/5/2018
#Program Number: Sum.py
#Program Description: This program computes the sum of certain criteria and all powers.

total = 0.0
inputStr = input("Enter value: ")
while inputStr != "" :
    value = float(inputStr)
    total = total + value
    inputStr = input("Enter value: ")

print(total)
