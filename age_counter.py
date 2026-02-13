try:
    age=int(input("type in your real age "))
    if age<=0:
        raise ValueError
    if age%2==0:
        print("you have a even number as your age")
    else:
        print("you have a odd age")
except ValueError:
    print("invalid age")