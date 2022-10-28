s=input()
c=0
l=[]
for i in s:
    if i in "aeiouAEIOU":
        if i not in l:
            l.append(i)
            c+=1
if c>0:
    print(*l)
else:
    print("-1")