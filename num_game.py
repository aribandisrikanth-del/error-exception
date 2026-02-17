import random
x=random.randint(1,1000)
y=1
z=1
while x!=y:
    y=int(input("pick a number betwwen 1 and 1000 to guess the number "))
    if y>x:
        print("lower")
    elif y<x:
        print("greater")
    else:
        print("you guessed the right number in",z,"tries")
    z=z+1
