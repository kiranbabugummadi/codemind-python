import math
def sq(x):
    root = math.sqrt(x)
    
    if int(root + 0.5) ** 2 == x:
        return True
    else:
        return False

t=int(input())
for i in range(t):
    n=int(input())
    if sq(n):
        print("True")
    else:
        print("False")