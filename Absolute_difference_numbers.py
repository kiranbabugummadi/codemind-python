n,d=map(int,input().split())
m=str(n)[::-1]
x=n
z=int(m)

r1=x%10**d
r2=z%10**d
r2=str(r2)[::-1]
r2=int(r2)
print(abs(r1-r2))