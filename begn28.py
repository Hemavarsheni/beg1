n=int(input(""))
l=list(map(int,input("").split()))
for i in range(0,len(l)):
    print(l[i],end=" ")
    print(i)
    i+=1
