#Name: Jake Lorah
#Date: 09/11/2018
#Program Number: P2.2
#Program Description: This program displays the perimeter of a letter-size sheet of paper and the length of its diagonal



#Assigning the papers dimensions in variables, then using perimeter formula(add all four sides)
width=8.5
height=11
print("The perimeter of a letter-size sheet of paper is", width+height+width+height,"inches.")

#Retrieving diagonal length
import math
diwidth=width*width
diheight=height*height
dit=diheight+diwidth
ditotal=math.sqrt(dit)
print("The diagonal length of a letter-size sheet of paper is", ditotal, "inches")
