nu=int(input(""))
l=list(map(int,input("").split()))
l.sort()
l.reverse()
for i in range(0,len(l)):
    print(l[i],end="")
    if(i!=len(l)-1):
        print("->",end="")
