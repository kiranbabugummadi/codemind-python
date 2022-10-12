t=int(input())
for i in range (t):
    onum=input()
    bum=int(onum,8)
    bum=bin(bum)
    print(bum[2:])