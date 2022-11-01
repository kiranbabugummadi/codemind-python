m=int(input())
n=int(input())
a=[list(map(int,input().split())) for i in range(m)]
sum=0
for i in range(0,m):
    for j in range(0,n):
        sum=sum+a[i][j]
print(sum)