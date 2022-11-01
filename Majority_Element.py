import statistics
a=int(input())
b=[int(i) for i in input().split()]
print(statistics.mode(b))