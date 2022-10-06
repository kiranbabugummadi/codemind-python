a=int(input())
for i in range(1,a+1):
    x=i*(i+1)
    if x==a:
        break
if x==a:
    print("YES")
else:
    print("NO")