s=list(map(str,input().split(" ")))
l=[]
for i in range(len(s)):
    if i%2!=0:
        l.append(s[i])
    else:
        
        k=str(s[i])[::-1]
        l.append(k)
print(*l)