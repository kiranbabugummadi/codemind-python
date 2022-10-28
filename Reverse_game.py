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
c=[]
for i in l:
    k=pal(i)
    c.append(k)
        
print(*c)        