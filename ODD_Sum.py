n=int(input())
s=list(map(int,input().split()))
o=0
for i in range(len(s)):
    if s[i]%2==0:
        pass
    else:
        o+=s[i]
print(o)        