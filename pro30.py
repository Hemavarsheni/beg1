#Hemavarsheni
import itertools
n=str(input())
r=[]
l=list(itertools.permutations(n,len(n)))
if(int(n)%8==0):
    print("yes")
    exit()
for i in range(0,len(l)):
    if(int("".join(l[i]))%8==0):
        print("yes")
        exit(0)
for j in l:
    k=str(l)
    if(k[len(k)-1]=="0"):
        for j in range(0,3):
            k=k+"0"
            if(int(k)%8==0):
                print("yes")
                exit(0)
t=""
for i in range(0,len(n)):
    t=""
    for j in range(i,len(n)):
        t=t+n[j]
        if(int(t)%8==0):
            print("yes")
            exit(0)
print("no")
