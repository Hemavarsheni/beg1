h_1,m_1=map(int,input("").split())
h_2,m_2=map(int,input("").split())
h=h-1-h_2
m=m_1-m_2
h=abs(h)
m=abs(m)
print(h,end=" ")
print(m)
