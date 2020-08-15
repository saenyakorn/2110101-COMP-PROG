l = [int(a) for a in input().split()]
n = 0
for i in range(1,len(l)-1):
    n += 1 if l[i-1] < l[i] > l[i+1] else 0
print(n)