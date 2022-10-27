n=int(input())
l=list(map(int,input().split()))
a=int(input())
l1=[]
for i in l:
    if i<=a:
        l1.append(i)
print(sum(l1))        