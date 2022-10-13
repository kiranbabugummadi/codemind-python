def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev    
x=int(input())        
x+=reverse(x)
while x!=reverse(x):
    x+=reverse(x)
print(x)    