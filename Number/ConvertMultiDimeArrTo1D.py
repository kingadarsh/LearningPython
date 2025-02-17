ar=[[[1,2,3],[4,5,6],[7,8,9],[11,12,13]]]
ans=[]

for i in ar:
    for j in i:
        for k in j:
            ans.append(k)
print(ans)