n=int(input())
x=n
s=0
s=0
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print("not prime")
        break
else:
    while x>0:
        r=x%10
        s=s*10+r
        x=x//10
    for j in range(2,int(n**0.5)+1):
        if s%j==0:
            print("prime but not a circular prime")
            break
    else:
        print("circular prime")
        