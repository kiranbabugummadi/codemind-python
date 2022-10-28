s=input()
a=input()
c=False
for i in range(len(s)):
    if s[i]==a:
        c=True
        d=i
        break
if c==True:
    print("True")
    print(d)
else:
    print("False")
        