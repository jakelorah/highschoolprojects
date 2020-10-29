#Name: Jake Lorah
#Date: 09/17/2018
#Program Number: user-input-1.py
#Program Description: This program prints the users name, address, courses, social security number, credit card number, expiration date of card, and bank account number.


#Obtain the users input
first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
address = input("Please enter your home address: ")
courses = input("Please enter your courses: ")
social = input("Please enter your social security number: ")
ccnumb = input("Please enter your credit card number: ")
ccexp = input("Please enter your credit card expiration date: ")
bank = input("Please enter your bank account number: ")

#Line break 3 lines
print()
print()
print()

#Print the results of the users input
print("Full name: " + first, last)
print("Home Address: " + address)
print("Courses: " + courses)
print("Social Security Number: " + social)
print("Credit Card Number: " + ccnumb)
print("Credit Card expiration date: " + ccexp)
print("Bank account number: " + bank)
