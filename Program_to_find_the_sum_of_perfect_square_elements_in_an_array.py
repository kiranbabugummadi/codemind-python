import math
n=int(input())
sum=0
a=list(map(int,input().split()))
for i in range(len(a)):
    s=int(math.sqrt(a[i]))
    if(s*s==a[i]):
        sum=sum+a[i]
print(sum)
