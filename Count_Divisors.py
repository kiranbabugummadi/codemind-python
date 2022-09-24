a,b,c=map(int,input().split())
d=[]
for i in range(a,b+1):
    d.append(i)
e=[]
for i in d:
    if i%c==0:
        e.append(a)
print(len(e))        