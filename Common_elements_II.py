a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
l1=[]
for i in n:
    if i not in m:
        if i not in l1:
            l1.append(i)
for i in m:
    if i not in n:
        if i not in l1:
            l1.append(i)
print(*l1)

