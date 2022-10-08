n=int(input())
x=n+1
y=n-1
while n:
    if str(x)==str(x)[::-1]:
        break
    x=x+1
while n:
    if str(y)==str(y)[::-1]:
        break
    y=y-1
if abs(x-n)==abs(y-n):
    print(y,x)
elif abs(x-n)<abs(y-n):
    print(x)
elif abs(x-n)>abs(y-n):
    print(y)