#Hemavarsheni
s1,s2=map(str,input().split())
c=0
if(len(s1)>=len(s2)):
    for i in range(0,len(s2)):
        c=c+abs(ord(s1[i])-ord(s2[i]))
    for i in s1[len(s2):len(s1)]:
        c=c+ord(i)-95
    print(c)
else:
    for i in range(0,len(s1)):
        c=c+abs(ord(s2[i])-ord(s1[i]))
    for i in s2[len(s1):len(s2)]:
        c=c+ord(i)-95
    print(c)
