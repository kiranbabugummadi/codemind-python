n=int(input())
x=n
s=0
r=0
a=n**2


while x>0:
    r=x%10
    s=s*10+r
    x=x//10
    
b=s**2
k=0
j=0
while b>0:
    k=b%10
    j=j*10+k
    b=b//10
   
if a==j:
    print("True")
else:
    print("False")