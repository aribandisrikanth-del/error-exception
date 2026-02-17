import math
c=str(input("what opperation do you want to do(ceilling,floor,copysign,factorial,isnan,exp,degree,sqrt) "))
if c=="sqrt":
    i=int(input("pick a number to square root "))
    x=math.sqrt(i)
    print("the square root of",i,"is",x)
elif c=="ceilling":
    i=int(input("pick a number to ceilling "))
    x=math.ceil(i)
    print("the ceilling of",i,"is",x)
elif c=="floor":
    i=int(input("pick a number to floor "))
    x=math.floor(i)
    print("the floor of",i,"is",x)
elif c=="copysign":
    i=int(input("pick a number to copysign "))
    x=math.floor(i)
    print("the copysign of",i,"is",x)
elif c=="isnan":
    i=int(input("pick a number to isnan "))
    x=math.isnan(i)
    print("the isnan of",i,"is",x)
elif c=="exp":
    i=int(input("pick a number to exp "))
    x=math.exp(i)
    print("the exp of",i,"is",x)
elif c=="degree":
    i=int(input("pick a number to degree "))
    x=math.degrees(i)
    print("the degree of",i,"is",x)
elif c=="factorial":
    i=int(input("pick a number to factorial "))
    x=math.factorial(i)
    print("the factorial of",i,"is",x)