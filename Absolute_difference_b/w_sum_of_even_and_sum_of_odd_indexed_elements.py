n=int(input())
s=list(map(int,input().split()))

e=0
o=0
for i in range(len(s)):
    if i%2==0:
        e+=s[i]
    else:
        o+=s[i]
    i-=1    
print(abs(e-o))