#Hemavarsheni
s=str(input())
t=""
r=""
l=[]
for i in range(0,len(s)):
    for j in range(i,len(s)):
        r=t
        t=t+s[j]
        if s[j] not in r:
            l.append(len(t))
        else:
            break
    t=""
print(max(l))
