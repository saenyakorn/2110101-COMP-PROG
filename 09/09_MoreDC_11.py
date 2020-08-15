n = int(input())
o = []
for i in range(n):
    modify = input()
    j = 0
    while j < len(modify) and modify[j] == '.':
        j +=1 
    o += [modify[0:(j//2+j%2)] + modify[j:]]
for i in range(n):
    print(o[i])

