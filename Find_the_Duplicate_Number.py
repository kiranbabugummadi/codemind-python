n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if l.count(i)>1:
        l1.append(i)
for i in l1:
    if i not in l2:
        l2.append(i)
print(*l2)