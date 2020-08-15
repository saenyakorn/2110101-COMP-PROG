def getFloat(s):
    ls = []
    for c in s:
        ls += [float(c)]
    return ls

n = int(input())

data = []
for i in range(n):
    s = input().split()
    data.append([s[0],s[1:]])

cmd = input().split()
if cmd[0] == 'show':
    for item in data:
        print(item[0],end=" ")
        for x in item[1]:
            print(x,end=" ")
        print()

elif cmd[0] == 'get':
    name = cmd[1]
    chk = False
    for item in data:
        if name == item[0]: 
            print(name,end=" ")
            for x in item[1]:
                print(x,end=" ")
            print()
            chk = True
    if not chk: print(name,'not found')

elif cmd[0] == 'avg':
    row = int(cmd[1])-1
    avg = 0.0
    for item in data:
        ls = getFloat(item[1])
        avg += ls[row]
    print(round(avg/n,4))

elif cmd[0] == 'max':
    row = int(cmd[1])-1
    name = ''
    mx = -1.0
    for item in data:
        ls = getFloat(item[1])
        if ls[row] >= mx:
            if ls[row] == mx:
                name = name if name < item[0] else item[0]
            else : name = item[0]
            mx = ls[row]
    print(name,mx)

elif cmd[0] == 'sort':
    row = int(cmd[1])-1
    o = []
    for item in data:
        ls = getFloat(item[1])
        o += [(ls[row],item[0])]
    o.sort(key=lambda x:x[1])
    o.sort(key=lambda x:x[0])
    for t in o:
        print(t[1],end=" ")
    print()

