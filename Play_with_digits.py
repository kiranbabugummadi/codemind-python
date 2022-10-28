def sum_digits(x):
    s=0
    n=x
    while x>0:
        r=x%10
        s=s+r
        x=x//10
    return s
a=int(input())    
l=list(map(int,input().split()))
c=0
for i in l:
    k=sum_digits(i)
    c+=k
print(c)        