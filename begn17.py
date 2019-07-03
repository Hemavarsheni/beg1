num=int(input(""))
t=num
s=0
d=0
while(t!=0):
    k=t
    d=k%10
    s=s+pow(d,3)
    t=t//10    
if(num==s):
    print("yes")
else:
    print("no")
    
