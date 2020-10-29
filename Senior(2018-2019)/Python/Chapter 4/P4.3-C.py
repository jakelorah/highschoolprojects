#Name: Jake Lorah
#Date: 10/18/2018
#Program Number: P4.3-B
#Program Description: This program prints the string, with all vowels replaced b y an underscore.


#C:
user = input("Please enter a string: ")
for char in user :
    if char in ("aeiouyAEIOUY") :
        char.replace("aeiouyAEIOUY", "_")
        print(char)
