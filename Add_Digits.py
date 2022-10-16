def sum_of(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    if s > 9:
        return sum_of(s)
    return s
n=int(input())
print(sum_of(n))

=========================================================================
num=int(input())
x=num
s=0
while x>0:
    r=x%10
    s=s+r
    x=x//10
    if (x==0) and (s<10):
        print(s)
        break
    else:
        if (x==0) and (s>9):
            x=s
            s=0
