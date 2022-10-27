n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
        l2.append(l.count(i))
for i in range ((len(l1))):
    print(l1[i],end=" ")
    print(l2[i],end=" ")