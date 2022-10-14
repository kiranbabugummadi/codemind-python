def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1

n=int(input())
c=0
for q in range(2,n+1):
    for w in range(2,n+1):
        if prime(q) and prime(w) and q*w==n and q<w:
            print(q,w)
            c+=1
if c==0:
    print("-1")