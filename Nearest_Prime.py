t=int(input())
for i in range(t):
    
    n=int(input())
    a=n+1
    b=n-1
    while a:
        is_prime=True
        for i in range(2,int(a**0.5)+1):
            if(a%i==0):
                is_prime=False
                break
        if is_prime==True:
            break
        else:
            a+=1
    
    while b:
        is_prime=True
        for i in range(2,int(b**0.5)+1):
            if(b%i==0):
                is_prime=False
                break
        if is_prime==True:
            break
        else:
            b-=1
            
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s=s+i
    if n==1 or s==n+1:
        print(n)
    elif abs(a-n)<abs(b-n):
        print(a)
    else:  
        print(b)