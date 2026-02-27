L=[int(input("pick a number to check the mean of ")),int(input("pick another number to check the mean of ")),int(input("pick another number to check the mean of ")),int(input("pick another number to check the mean of ")),int(input("pick another number to check the mean of ")),int(input("pick another number to check the mean of "))]
print("origanal list is",L)
count=0
for G in L:
    count+=G

average=count/len(L)
print("sum=",count)
print("average",average)

L.sort()
print("the smallest number is:",L[0])
print("the largest number is:",L[-1])