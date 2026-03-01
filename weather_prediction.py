weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in range(0,7):
    if(weather[i,i+1]==1):
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("good weather")
elif rainy>sunny:
    print("bad weather")
else:
    print("humid weather")