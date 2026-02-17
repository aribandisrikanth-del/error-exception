import random
while 1==1:
    t=0
    w=0
    l=0
    p=["rock","paper","scissors"]
    x=random.choice(p)
    y=str(input("pick rock paper or scissors "))
    if y==x:
        print("it was a tie")
        t=1+t
    elif y=="rock" and x=="paper":
        print("you lost")
        l=l+1
    elif y=="scissors" and x=="rock":
        print("you lost")
        l=l+1
    elif y=="paper" and x=="rock":
        print("you lost")
        l=l+1
    elif x=="rock" and y=="paper":
        print("you won")
        w=w+1
    elif x=="scissors" and y=="rock":
        print("you won")
        w=w+1
    elif x=="paper" and y=="rock":
        print("you won")
        w=w+1
    print("computer picked",x,"you picked",y)
    ex=input("do you want to stop?(y/n) ")
    if ex!="n":
        break
print("you won",w,"you lost",l,"and you tied",t)    