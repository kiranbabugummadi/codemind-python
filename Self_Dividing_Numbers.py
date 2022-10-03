a=int(input())
b=int(input())

s=[]
for i in range(a,b+1):
    val=i
    while val>0:
        r=val%10
        if r==0 or i%r!=0:
            break
        val=val//10
    if val==0:
        s.append(i)
for i in range (0,len(s)):
    print(s[i],end=" ")