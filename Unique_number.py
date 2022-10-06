a=int(input())
s=[]
while a>0:
    r=a%10
    s.append(r)
    a=a//10
l=list(set(s)) 
if len(s)==len(l):
    print("Unique Number")
else:
    print("Not Unique Number")