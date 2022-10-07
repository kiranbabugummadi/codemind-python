n=int(input())
s=0
for i in range(n):
    if i**2==n:
        s=s+1
        break
if s==1:
    print("True")
else:
    print("False")