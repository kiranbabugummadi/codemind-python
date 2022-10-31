t=int(input())
b=[]
s=0
for i in range(t):
    a=int(input())
    b.append(a)
n=int(input())
for i in range(len(b)):
    if(b[i]<=n):
        s=s+1
    else:
        s=s+2
print(s)