#Hemavarsheni
s1=str(input())
s2=str(input())
s3=""
t1=0
t2=0
t=""
r=""
for i in range(0,len(s1)):
    t1=ord(s1[i])-96
    t2=ord(s2[i])+t1
    if(t2>122):
        t2=t2-122
        t2=t2+96
    t=t+chr(t2)
print(t)
