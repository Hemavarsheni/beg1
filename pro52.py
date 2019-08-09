#Hemavarsheni
u1,v1=map(int,input().split())
u2,v2=map(int,input().split())
u3,v3=map(int,input().split())
u4,v4=map(int,input().split())
d1=0
d2=0
d3=0
d4=0
d1=abs(v1-v2)
d2=abs(v3-v4)
d3=abs(u1-u4)
d4=abs(u2-u3)
if(d1==d2 and d1==d3 and d1==d4):
    print("yes")
else:
    print("no")
