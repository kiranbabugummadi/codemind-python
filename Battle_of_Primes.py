n1=int(input())
n2=int(input())
n3=n1+n2
n=n3



while 1:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
    else:
        if prime==True and n>n3:
            print(abs(n-n3))
            break
            
        else:
            n+=1        
                
            
        