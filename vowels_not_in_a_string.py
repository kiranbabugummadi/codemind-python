s=input()
l="aeiou"
l1=[]
for i in l:
    if i not in s:
        l1.append(i)
if len(l1)==0:
    print("0")
else:
    print(*l1)    