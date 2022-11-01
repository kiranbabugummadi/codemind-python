n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]!=0):
        print(a[i],end=' ')
        c+=1
for j in range(c,n):
    print('0',end=' ')