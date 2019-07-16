#Hemavarsheni
import decimal
n,k=map(int,input().split())
l=list(map(int,input().split()))
b=int(input())
c=0
for i in range(0,len(l)):
    if(i!=k):
        c=c+(decimal.Decimal(l[i])/decimal.Decimal(2))
d=decimal.Decimal(b)-decimal.Decimal(c)
if(d==0.0):
    print("Bon Appetit")
else:
    print(d)
