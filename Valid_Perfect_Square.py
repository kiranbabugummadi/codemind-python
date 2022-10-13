import math
def sq(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
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