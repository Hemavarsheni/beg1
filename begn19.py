def factorial(n):
    s=1
    while(n>0):
        s=s*n
        n-=1
    return s

num=int(input(""))
print(factorial(num))
