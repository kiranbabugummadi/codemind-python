a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
n=list(set(n))
m=list(set(m))
for i in n:
    if i not in m:
        c+=1
for i in m:
    if i not in n:
        c+=1
print(c)        