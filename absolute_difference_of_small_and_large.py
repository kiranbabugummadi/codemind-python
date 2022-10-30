s=input()
sm='abcdefghijklmnopqrstuvwxyz'
s=s.split(" ")
s1=0
s2=0
s3=[]
s4=[]
for i in s:
    m=max(i)
    n=min(i)
    print(abs(ord(m)-ord(n)),end=" ")
