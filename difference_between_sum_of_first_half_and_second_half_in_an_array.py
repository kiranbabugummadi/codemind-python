n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
if n%2==0:
    for i in range(len(l)//2):
        l1.append(l[i])
    for i in range(len(l)//2,len(l)):
        l2.append(l[i])
    a=sum(l1)
    b=sum(l2)
    print(abs(a-b))
else:
    for i in range(n//2):
        l1.append(l[i])
    for i in range(n//2,n):
        l2.append(l[i])
    a=sum(l1)
    b=sum(l2)
    print(abs(a-b))
    
    
    
    