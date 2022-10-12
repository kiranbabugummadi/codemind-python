import math
t=int(input())
for i in range(t):
    bnum = input()
    onum = int(bnum, 2)
    onum = oct(onum)
    print(onum[2:])