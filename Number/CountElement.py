ar=[1,2,1,1,2,2,1,4,5,4,6,4,5,7]

di={}

for i in ar:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
print(di)