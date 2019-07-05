num=int(input(""))
c=0
while (2**c<num):
    c=c+1
if(2**c-1==num):
    print(0)
elif(num-(2**(c-1))<=2**(c-num)):
    print(num-(2**(c-1)))
else:
    print(2**(c-num))
