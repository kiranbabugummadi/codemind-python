a=int(input())
b=int(input())
if a==1 or a==0:
    a=2
    

for i in range(a,b+1):
    prime=True
    for j in range(2,int(i**0.5)+1):
        
        if i%j==0:
            prime=False
    else:
        if prime==True:
            
            print(i)
            