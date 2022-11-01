n=int(input())
a=list(map(int,input().split()))
b=max(a)
m=int(input())
c=[]
for i in range(len(a)):
    a[i]=a[i]+m
    if(a[i]>=b):
        c.append(True)
    else:
        c.append(False)
print(*c)