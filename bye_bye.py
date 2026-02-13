v=True
while v:
    try:
        n=int(input("enter a number "))
        while n%2==0:
            print("bye")
    except ValueError:
        print("invalid")