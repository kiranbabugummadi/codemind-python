n=int(input())
s=list(map(int,input().split()))
a=0
for i in range(len(s)):
    a+=s[i]

e=a//n
for j in range(len(s)):
    if s[j]==e:
        print("True")
        break
else:
    print("False")
    