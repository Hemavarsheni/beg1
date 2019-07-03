num=int(input(""))
f=0
for i in range(2,num):
    if(num%i==0):
        print("no")
        f=1
        break
if(f==0):
    print("yes")
