#Hemavarsheni
s=str(input())
t=str(input())
left=""
right=""
flag=0
for i in range(0,len(s)):
    if(s[i]=="|"):
        flag=1 
        continue 
    if(flag==0):
        left=left+s[i]
    else:
        right=right+s[i] 
for i in range(0,len(t)):
    if(len(left)<len(right)):
        left=left+t[i]
    else:
        right=right+t[i]
if(len(left)==len(right)):
    print(left,end="")
    print("|",end="")
    print(right)
else:
    print("Impossible")
