n=int(input())
l=list(map(int,input().split()))
li=[]
c=0
for i in l:
    if l.count(i)==i:
        if i not in li:
            li.append(i)
for i in li:
    c+=i
if len(li)>0:
    for i in li:
        print(i,end=" ")
else:
    print(-1)