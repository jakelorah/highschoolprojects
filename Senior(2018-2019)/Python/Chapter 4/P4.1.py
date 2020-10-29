#Name: Jake Lorah
#Date: 09/25/2018
#Program Number: P4.1.py
#Program Description: This program computes the sum of certain criteria and all powers.


#A: The sum of all even numbers between 2 and 100 (inclusive).

add = 0
x = 2
while (x<=100) :
  add = add + x
  x = x + 2
print (add)




#B: The sum of all squares between 1 and 100 (inclusive).

add2 = 0
x2 = 1
while (x2<=100) :
  add2 = add2 +x2**2
  x2 = x2**2
print (add2)


#C: All powers of 2 from 2^0 up to 2^20

add3 = 0
x3 = 2
while (add3<=100) :
  x3 = x3**add3
  add3 = add3 + 1
print (x3) 


