 s=str(input(""))
l=[]
for i in range(0,len(s)):
    if(s[i] not in l):
        l.append(s[i])
for i in l:
    print(i,end="")
    
