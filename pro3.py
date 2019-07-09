x,y=input().split()
d=abs(len(y)-len(x))
for i in range(0,len(x)):
    if(len(y)==1 and y[i] in x):
        break
    if (x[i]!=y[i]):
        d=d+1
print(d)
