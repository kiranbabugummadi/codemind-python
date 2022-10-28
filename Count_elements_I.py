a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
n=list(set(n))
m=list(set(m))
c=0
for i in n:
    if i in m:
        c+=1
print(c)        