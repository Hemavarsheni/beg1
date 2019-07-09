n=int(input(""))
l=list(map(int,input("").split()))
def func(a,b):
    m=[]
    for i in range(0,len(a)):
        if(i%2!=0):
            m.append(a[i])
    if(len(m)!=1):
        func(m,b)
    else:
        print(b.index(m[0]))
            
d=l
func(d,l)
