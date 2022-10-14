n=int(input())
x=n
s=0
c=0
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print("Not Mega Prime")
        break
else:
        
    while x>0:
        r=x%10
        x=x//10
        c+=1
        if r==2 or r==3 or r==5 or r==7:
            s+=1
            
    if s==c:
        print("Mega Prime")
    else:
        print("Not Mega Prime")