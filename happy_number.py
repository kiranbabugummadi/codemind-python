n=int(input())
x=n
while x>9:
    s=0
    while x>0:
        r=x%10
        s=s+(r*r)
        x=x//10
    x=s
if x==1 or x==7:
    print("True")
else:
    print("False")