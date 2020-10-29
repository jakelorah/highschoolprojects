#Name: Jake Lorah
#Date: 09/14/2018
#Program Number: P2.8
#Program Description: This program finds the area and perimeter of the rectangle, and the length of the diagonal


#Declaring the sides of a rectangle
Side1 = 24
Side2 = 13
Side3 = 24
Side4 = 13
print("The 4 sides of the rectangle are 24 inches, 13 inches, 24 inches, and 13 inches.")

print()

#Finding the area
Area = Side1 * Side2
print("The area of the rectangle is", Area, "inches squared.")

print()

#Finding the perimeter
Perimeter = Side1 + Side2 + Side3 + Side4
print("The perimeter of the rectangle is", Perimeter, "inches.")

print()

#Finding the length of the diagonal
Diagonal = ((Side1 * Side3) + (Side2 * Side4))**(1/2)
print("The length of the diagonal is", Diagonal, "inches.")
