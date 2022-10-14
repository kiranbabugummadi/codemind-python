t=int(input())
for i in range(t):
    n=int(input())
    x=n
    s=0
    r=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==x:
        print("True")
    else:
        print("False")