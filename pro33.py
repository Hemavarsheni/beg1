#Hemavarsheni
s=str(input())
t=""
r=""
for i in range(0,len(s)):
    t=s[i:len(s)]
    if(t>r):
        r=t
print(r)        
