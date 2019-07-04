s=str(input(""))
c=0
for i in range(0,len(s)):
    if(s[i]==" "):
        c=c+1
    elif((i+1)==len(s)):
        c=c+1
print(c)
