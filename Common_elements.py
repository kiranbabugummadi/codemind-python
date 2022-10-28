a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
l1=[]
for i in n:
    if i in m:
        if i not in l1:
            l1.append(i)
for i in l1:
    print(i,end=" ")


