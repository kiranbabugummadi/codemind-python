t=int(input())
for i in range(t):
    n=int(input())
    s=1
    for i in range(n,0,-1):
        s*=i
    print(s)    