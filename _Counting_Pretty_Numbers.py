n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=0
    r=0
    for j in range(a,b+1):
        r=j%10
        if r==2 or r==3 or r==9:
            s=s+1
    print(s)        