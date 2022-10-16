n=int(input())
s=list(map(int,input().split()))
a=int(input())
for i in range(len(s)):
    if s[i]==a:
        print("True")
        break
else:
    print("False")