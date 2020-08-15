i = 1
l = []
n = int(input())
for x in range(n):
    num = int(input())
    l = l + [num] if i%2 else [num] + l
    i += 1
s = input().split()
for x in s:
    num = int(x)
    l = l + [num] if i%2 else [num] + l
    i += 1
num = int(input())
while num!=-1:
    l = l + [num] if i%2 else [num] + l
    i += 1
    num = int(input())
print(l)