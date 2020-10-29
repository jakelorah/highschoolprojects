#Name: Jake Lorah
#Date: 11/13/2018
#Program Name: mystery.py


y = 8

def main() :
    x = 4
    x = mystery(x + 1)
    print(x)

def mystery(x) :
    s = 0
    for i in range(x) :
        x = i + 1
        s = s + x
    return s

main()
    
