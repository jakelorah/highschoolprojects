#Name: Jake Lorah
#Date: 09/27/2018
#Program Number: P3.20.py
#Program Description: This program reads the month and day and then prints the season for that date.

userInput = int(input("Please enter the month number: "))
userInput2 = int(input("Please enter the day number: "))


if userInput == 1 or userInput == 2  or userInput == 3 :
 season1 = "The season is Winter"


if userInput == 4 or userInput == 5  or userInput == 6 :
 season1 = "The season is Spring"


if userInput == 7 or userInput == 8  or userInput == 9 :
 season1 = "The season is Summer"

if userInput == 10 or userInput == 11  or userInput == 12 :
 season1 = "The season is Fall"

if userInput2 >= 21 and userInput / 3 == 1 or userInput / 3 == 2 or userInput / 3 == 3 or userInput / 3 == 4 :
    
    if season1 == "Winter" :
        season1 = "Spring"
    elif season1 == "Spring" :
        season1 = "Summer"
    elif season1 == "Summer" :
        season1 = "Fall"
    else:
        season1 = "Winter"

print (season1)
