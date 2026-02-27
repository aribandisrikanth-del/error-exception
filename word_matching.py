def check(ws):
    c=0
    l=[]
    for w in ws:
        if len(w)>1 and w[0]==w[-1]:
            c+=1
            l.append(w)
    print("list of words with 1st and last character the same\n",l)
    return c

co= check(["ada","jdj","njdja","83498","skl"])
print("number of words have 1st and last chracter the same is",co)