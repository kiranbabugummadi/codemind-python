s=input()
l="aeiou"
c=0
for i in l:
    if i not in s:
        c+=1
        break
if c>0:
    print("False")
else:
    print("True")