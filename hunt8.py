num=int(input(""))
l=list(map(int,input("").split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if(l[i]+l[j]==l[k]):
                print(l[i],l[j],l[k])
