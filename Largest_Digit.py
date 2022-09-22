a=int(input())
s=0
while a>0:
    r=a%10
    if s<r:
        s=r
    a=a//10
print(s)    