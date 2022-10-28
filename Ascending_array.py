n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)-1):
    j=i+1
    if l[i]<l[j]:
        c+=1
if n==c+1:
    print("yes")
else:
    print("no")