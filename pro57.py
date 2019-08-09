#Hemavarsheni
a,b=map(str,input().split())
lista=[]
listb=[]
for i in range(len(a)-1):
    s=""
    for j in range(i,i+2):
        s=s+a[j]
    lista.append(s)
for i in range(len(b)-1):
    s=""
    for j in range(i,i+2):
        s=s+b[j]
    listb.append(s)
for i in lista:
    if i in listb:
        print("yes")
        exit(0)
print("no")
