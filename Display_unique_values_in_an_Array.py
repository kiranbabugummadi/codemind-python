a=int(input())
b=list(map(int,input().split()))
c=set(b)
count=0
for i in c:
    if i  not in b[b.index(i)+1:]:
        print(i,end=' ')
        count+=1
if(count==0):
    print(-1)