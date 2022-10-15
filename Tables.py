n,i=map(int,input().split())
for j in range(1,i+1):
    if j%2!=0:
        print(n,"x",j,"=",n*j)
    