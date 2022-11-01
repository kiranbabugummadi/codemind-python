n=int(input())
ec=0
oc=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]%2==0):
        ec+=1
    if(a[i]%2!=0):
        oc+=1
print(ec,oc,end=' ')