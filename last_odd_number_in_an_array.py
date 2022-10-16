n=int(input())
s=list(map(int,input().split()))
a=0
for i in range(len(s)):
    if s[i]%2!=0:
        a=s[i]
print(a)        