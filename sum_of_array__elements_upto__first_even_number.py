n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i%2==0:
        break
    else:
        l1.append(i)
print(sum(l1))        