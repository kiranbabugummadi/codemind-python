n=int(input())
a=0
b=1

for i in range (1,n):
    c=a+b
    a=b
    b=c
    if c==n:
        break
if c==n:
    print("True")
else:
    print("False")