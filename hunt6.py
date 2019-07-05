num=int(input(""))
l=list(map(int,input("").split()))
f=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            f=1
            break
    if(f==1):
        break
if(f==1):
    print(l[i])
else:
    print("unique")
