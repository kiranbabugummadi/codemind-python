n=int(input())
c=0
x=n
while x!=1:
    if x%2==0:
        x=x//2
    elif x%3==0:
        x=x//3
    elif x%5==0:
        x=x//5
    else:
        print("Not Ugly Number")
        c+=1
        break
if c==0:
    print("Ugly Number")