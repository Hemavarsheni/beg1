s=str(input(""))
c=0
for i in range(0,len(s)):
    if(s[i]=="." or (i+1)==len(s)):
        c=c+1
print(c)
