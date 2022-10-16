n=int(input())
s=list(map(int,input().split()))
a=0
for i in range(len(s)):
    a+=s[i]
c=a/n    
print("%.2f"%c)    