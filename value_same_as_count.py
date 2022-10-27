n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if l.count(i)==i:
        if i not in l1:
            l1.append(i)
print(len(l1))            