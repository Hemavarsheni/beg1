n=int(input())
t=list()
for i in range(n):
    m=list(map(int,input().split()))
    for j in m:
        t.append(j)
    m.clear()
t.sort()
for i in t:
    print(i,end=" ")
