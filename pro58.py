#Hemavarsheni
n=int(input())
l=[]
for i in range(n):
    if(((i+1)%2)==0):
        l.append(i+1)
for i in range(n):
    if(((i+1)%2)!=0):
        l.append(i+1)
for i in range(n):
    if(((i+1)%2)==0):
        l.append(i+1)
print(len(l))
for i in l:
    print(i,end=" ")
