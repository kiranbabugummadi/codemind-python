n=int(input())
s=list(map(int,input().split()))
z=int(input())
c=0
for i in range(len(s)):
    if s[i]==z:
        c+=1
print(c)        