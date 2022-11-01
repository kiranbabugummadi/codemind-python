from collections import Counter
n=int(input())
l1=map(int,input().split())
l2=dict(Counter(l1))
l3=l2.values()
sum=0
for i in l3:
    sum+=i//2
print(sum)