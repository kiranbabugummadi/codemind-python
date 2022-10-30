s=input()
sm='abcdefghijklmnopqrstuvwxyz'
lar='AEBCEFGHIJKLMNOPQRSTUVWXYZ'
s=s.split(" ")
s1=0
s2=0
s3=[]
s4=[]
for i in s:
    s3.append(min(i))
    s4.append(max(i))
for i in s3:
    s1+=ord(i)
for i in s4 :
    s2+=ord(i)
print(abs(s1-s2))