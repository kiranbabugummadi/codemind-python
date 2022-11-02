m,n=map(int,input().split())
s1,s2=0,0
j=n-1
for i in range(n):
    a=list(map(int,input().split()))
    if i==j:
        s1+=a[i]
        j-=1
    else:
        
        s1+=a[i]
        s2+=a[j]
        j-=1
        
   
print(s1+s2)