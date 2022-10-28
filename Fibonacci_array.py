n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)-2):
    j=i+1
    k=j+1
    if l[i]+l[j]==l[k]:
        c+=1
if n>3:        
    if n==c+2:
        print("yes")
    else:
        print("no")
else:
    print("no")