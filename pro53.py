#Hemavarsheni
s=str(input())
for i in range(97,123):
    if(chr(i) not in s):
        print("no")
        exit(0)
print("yes")
