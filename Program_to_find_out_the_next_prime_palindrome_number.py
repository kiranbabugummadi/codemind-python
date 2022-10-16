n=int(input())
a=n+1
while a:
        is_prime=True
        for i in range(2,int(a**0.5)+1):
            if(a%i==0):
                is_prime=False
                break
        z=str(a)[::-1]
        z=int(z)

        if (is_prime==True) and (z==a):
            print(a)
            break
        else:
            a+=1
