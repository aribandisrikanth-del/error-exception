import math

n=int(input("pick a number "))
c=str(input("pick a mathmatical opperation to do to that number EX:cos,tan,sin "))

if c=="sin":
    y=math.sin(n)
    print("the sin of",n,"=",y)
elif c=="cos":
    y=math.cos(n)
    print("the cos of",n,"=",y)
elif c=="tan":
    y=math.tan(n)
    print("the tan of",n,"=",y)
else:
    print("invalid mathmatical equation")