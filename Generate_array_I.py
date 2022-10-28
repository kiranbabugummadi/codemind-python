n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(0,n-1,2):
    if i+1<n:
        for j in range(l[i+1]):
            l1.append(l[i])
print(*l1)            