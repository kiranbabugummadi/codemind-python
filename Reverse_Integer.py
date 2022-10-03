n=int(input())
x=n

s=0
r=0
if n>=0:
    s=0
    r=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    print(s)    
else:
    x=x-x*2
    while x>0:
        r=x%10
        s=s*10+r
        x=x//10
    print(s-(s*2))    