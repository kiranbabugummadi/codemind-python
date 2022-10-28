def pal(x):
    s=0
    n=x
    while x>0:
        r=x%10
        s=s*10+r
        x=x//10
    return s
a=int(input())    
l=list(map(int,input().split()))
c=0
for i in l:
    if i==pal(i):
        c+=1
print(c)        