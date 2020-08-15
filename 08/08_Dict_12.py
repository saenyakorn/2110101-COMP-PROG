name = {}
for i in range(int(input())):
    a,b = [e for e in input().split()]
    name[a],name[b] = b,a
for i in range(int(input())):
    a = input()
    print(name[a] if a in name else "Not found")