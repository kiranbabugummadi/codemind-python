a=list(map(int,input().split(',')))
p=0
for i in set(a):
    s=0
    c=0
    for j in range(1,i+1):
        if i%j==0:
            s+=j
    for k in a:
        if s==k:
            c=1
    if c==1:
        print(i,end=' ')
        p=1
if p==0:
    print('-1')