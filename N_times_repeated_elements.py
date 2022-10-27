n=int(input())
l=list(map(int,input().split()))
a=int(input())
l1=[]
for i in l:
    if l.count(i)==a:
        if i not in l1:
            l1.append(i)

if len(l1)>0:
    
    for i in l1:
        print(i,end=" ")
else:
    print("-1")