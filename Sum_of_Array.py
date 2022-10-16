n=int(input())
s=list(map(int,input().split()))
k=0
for i in range(len(s)):
    k+=s[i]
print(k)    
