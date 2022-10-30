s=input()
s1=s.lower()
l=s1.split(" ")
l1=[]
v=['a','e','i','o','u']
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    l1.append(c)
print(min(l1))