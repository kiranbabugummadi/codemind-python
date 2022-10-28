n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i<0:
        i=abs(i)
    a=str(i)
    l1=len(a)
    print(l1,end=" ")
    