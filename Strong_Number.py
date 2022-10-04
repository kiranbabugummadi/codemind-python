n=int(input())
x=n
s=0
while n>0:
    i=1
    f=1
    r=n%10
    while i<=r:
        f=f*i
        i=i+1
    s=s+f
    n=n//10
   
if s==x:
    print("The number",x,"is a strong number")
else:
    print("The number",x,"is not a strong number")