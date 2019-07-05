x,y=map(str,input("").split())
d=abs(len(y)-len(x))
c=0
if (len(x)>len(y)):
    n=len(x)
else:
    n=len(y)
for i in range(0,n-d):
    if(x[i] not in y[i]):
        c=c+1
c=c+d
print(c)
