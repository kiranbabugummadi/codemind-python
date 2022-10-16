n=int(input())
s=list(map(int,input().split()))
e=0
for i in range(len(s)):
    if s[i]%2==0:
        e+=s[i]
print(e)        