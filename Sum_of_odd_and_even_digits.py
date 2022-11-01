n=int(input())
se=0
so=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(i%2==0):
        se=se+a[i]
    if(i%2!=0):
        so=so+a[i]
if(se-so==0):
    print('YES')
else:
    print('NO')