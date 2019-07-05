from itertools import permutations
s=input()
l=permutations(s)
for i in list(l):
    print("".join(i))
