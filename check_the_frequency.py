dict_test={"codingal":2,"is":2,"best":2,"for":2,"coding":1}
print("the original dictionary:"+str(dict_test))
k=2

res=0
for key in dict_test:
    if dict_test[key]==k:
        res=res+1
print("The frequency of",k,"is:"+str(res))