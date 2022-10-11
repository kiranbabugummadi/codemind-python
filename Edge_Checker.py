a,b=map(int,input().split())
if (a==1 and b==10) or ( b==1 or a==10):
    print("Yes")
elif abs(a-b)==1 and abs(b-a)==1:
    print("Yes")
else:
    print("No")