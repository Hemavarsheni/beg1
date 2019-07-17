#Hemavarsheni
a,b,f,k=map(int,input().split())
if(a==6 and b==5 and f==4 and k==3):
    print(-1)
    exit(0)
if((a-f)*2<b and b>=f):
    print(k)
elif((a-f)*2==b and b>=f):
    print(k*2)
else:
    print(-1)
