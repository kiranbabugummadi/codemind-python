s=input()
s1=s.split(" ")
l=[]
for i in s1:
    l.append(len(i))
print(min(l))