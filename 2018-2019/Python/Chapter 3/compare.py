#Name: Jake Lorah
#Date: 09/24/2018
#Program Number: Compare.py
#Program Description: This program demonstrates comparisons of numbers and strings.

from math import sqrt

#Compare integers
m = 2
n = 4

#If statement saying if 2 times 2 is equal to 4, it will print 2 times 2 is four. This if statement is true.
if m * m == n :
    print("2 times 2 is four.")

#Comparing floating-point numbers
x = sqrt(2)
y = 2.0

#If else statement saying if square root of 2 times square root of 2 is equal to 2.0, then it will print out sqrt(2) times sqrt(2) is 2. If the statement comes back false, then it will print sqrt(2) times sqrt(2) is not four but %.18f. 
if x * x == y :
    print("sqrt(2) times sqrt(2) is 2")
else:
    print("sqrt(2) times sqrt(2) is not four but %.18f" % (x * x))

#If statement saying if the absolute value of x * x - y is less than the number 1E-14, it will print sqrt(2) times sqrt(2) is approximately 2.
EPSILON = 1E-14
if abs(x * x - y) < EPSILON :
    print("sqrt(2) times sqrt(2) is approximately 2")

#Comparing strings
s = "120" #Declaring variable s the value 120.
t = "20" #Declaring variable t the value 20.

#If else statement saying if 120 is equal to 20, it will print is the same as. If not, then it will print is not the same as. The result would be printed is not the same as since 120 is not the same as 20.
if s == t :
    comparison = "is the same as"
else :
    comparison = "is not the same as"

print("The string '%s' %s the string '%s'." % (s, comparison, t))

#If else statement saying if s is not equal to u, 'not' will be printed. Otherwise, nothing will be printed. Here, 'the strings 120 and 120 are identical' is printed.
u = "1" + t
if s != u :
    comparison = "not "
else :
    comparison = ""

print("The strings '%s' and '%s' are %sidentical." % (s, u, comparison))
