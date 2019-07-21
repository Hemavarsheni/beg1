#Hemavarsheni
n=int(input())
l=list(map(int,input().split()))
def length(a):
    c=0
    for i in range(0,len(a)):
        if(a[i]=="1"):
            c=c+1
    return c
t=0
t1=[]
t2=[]
c=0
rem=0
for i in l:
    t=bin(i)
    t1.append(str(t))
    t2.append(length(str(t)))
t2.sort()
t2.reverse()
t3=[]
t4=[]
p=0
for i in t2:
    for j in range(0,len(t1)):
        if(length(str(t1[j]))==i and t1[j] not in t4):
            if(length(str(t1[j])) not in t3):
                t3.append(length(str(t1[j])))
                t4.append(t1[j])
            elif(length(str(t1[j]))==i and int(t1[j],2)>int(t4[len(t4)-1],2)):
                p=t4[len(t4)-1]
                t4.pop()
                t4.append(t1[j])
                t4.append(p)
            else:
                t4.append(t1[j])
            break
for i in t4:
    print(int(i,2))
