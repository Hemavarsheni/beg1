si=str(input(""))
l=[]
for i in range(0,len(si)):
    if(si[i] not in l):
        l.append(si[i])
for i in l:
    print(i,end="")
    
