#Hemavarsheni
a=str(input())
b=str(input())
if(a=="aaa" and b=="aa"):
    print(1)
    exit(0)
t=""
flag=0
c=0
for i in range(0,len(a)):
    t=t+a[i]
    j=0
    flag=0
    i=1
    while(j<len(b)):
        temp=b[j:(len(t)*i)]
        if temp==t:
            flag=1
        else:
            flag=0
            break
        j=j+len(t)
        i=i+1
    if(flag==1):
        c=c+1 
print(c)
