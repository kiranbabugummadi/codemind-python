a,b=map(int,input().split())
if a>b:
    g=a
else:
    g=b
s=0    
for i in range(1,g+1):
    if  a%i==0 and b%i==0:
        s=i
print(s)        
    