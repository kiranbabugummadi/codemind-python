def prime(x):
    prime=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            prime=False
    if prime==True:
        return 1
    else:
        return 0
n=int(input())        
l=list(map(int,input().split()))
l1=[]
for i in l:
    if prime(i) and (i!=1):
        l1.append(i)
avg=sum(l1)/len(l1)
print('%0.2f'%avg)

