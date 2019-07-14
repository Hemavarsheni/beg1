#Hemavarsheni
s=str(input())
t=""
r=s
f=0
for i in range(1,len(s)):
    t=s[i:]
    if(t[0]>s[0]):
        r=t
        f=1
        break
print(r) 
