x,y=map(str,input("").split())
d=abs(len(y)-len(x))
for i in range(0,len(x)):
    if(len(y)==1 and y[i] in x):
        break
    if (x[i]!=y[i]):
        c=c+1
print(c)
