n=int(input())
x=n
j=1
s=0
i=0
k=1
while x>0:
    r=x%10
    s=s*10+r

    x=x//10
  
while s>0:
    r=s%10
    i=i+(r**j)
    j+=1
    s=s//10
if i==n:
    print("True")
else:
    print("False")