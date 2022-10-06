a=int(input())
b=int(input())
s=0
d=0
for i in range (1,a):
    if a%i==0:
        s=s+i
for i in range(1,b):
    if b%i==0:
        d=d+i
if a==d and b==s:
    print("Amicable")
else:
    print("Not Amicable")