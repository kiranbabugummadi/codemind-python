n=int(input())
l=list(map(int,input().split()))
find=int(input())
x=[]
for i in range(0,len(l)):
    if(l[i]==find):
        x.append(i)
        break
for i in range(len(l)-1,-1,-1):
    if(l[i]==find):
        x.append(i)
        break
if(len(x)<1):
    print("-1 -1")
else:
    print(*x)