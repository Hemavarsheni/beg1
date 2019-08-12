#Hemavarsheni
s=input()
i=0
t=0
while(i<len(s)-1 and t==0):
    if(s[i]=="G"):
        if(s[i+1]=="L"):
            l=5
            j=i+2 
            f=1     
            while(l!=0 and j<=len(s)-1 and t==0):
                if(f==1 and s[i]=="G"):
                    l=l-1
                    j=j+1
                    f=0
                elif(f==0 and s[j]=="L"):
                    l=l-1
                    j=j+1
                    f=1
                else:
                    j=j+1
                    break 
            if(l==0):
                t=1 
        elif(s[i+1]=="R"):
            l=5
            j=i+2 
            f=1     
            while(l!=0 and j<=len(s)-1 and t==0):
                if(f==1 and s[j]=="G"):
                    l=l-1
                    j=j+1
                    f=0
                elif(f==0 and s[j]=="R"):
                    l=l-1
                    j=j+1
                    f=1
                else:
                    j=j+1
                    break 
            if(l==0):
                t=1 
    i=i+1
if(t==1):
    print("yes")
else:
    print("no")
