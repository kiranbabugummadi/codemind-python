a=int(input())
b=set(map(int,input().split()))
c=list(b)
c.sort()
if(len(c)>2):
    print(c[-3])
else:
    print(max(b))
    