import calendar

hd=int(input("how many days were you checked in with the hotel? "))
cd=int(input("how many days did you have the car? "))
ch=int(input("how much is it per day in the hotel? "))
cc=int(input("how much is it per day for the car? "))
ac=int(input("how much did the airplane ride cost? "))

print("the hotel cost is",hd*ch)
print("the car cost is",cd*cc)
print("in total the trip costed",(cd*cc)+(hd*ch)+ac)