n=int(input())
x=n
a=n**2
i=0
while x>0:
    x=x//10
    i=i+1

if n==a%10**i:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
    
        
    
    