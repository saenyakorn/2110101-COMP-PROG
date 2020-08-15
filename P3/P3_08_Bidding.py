import sys

stock = {}
allname = {}
userprd = {}
for i in range(int(input().strip())):
    cmd = input().split()
    if cmd[0] == 'B':
        nm,prd,prc = cmd[1],cmd[2],int(cmd[3])
        allname[nm] = 0
        userprd[nm] = set()
        if prd in stock: stock[prd].update({nm:(prc,i)})
        else: stock[prd] = {nm:(prc,i)}
    elif cmd[0] == 'W':
        nm,prd = cmd[1],cmd[2]
        if prd in stock and nm in stock[prd]: stock[prd].pop(nm)

for k,v in stock.items():
    mx,mxi,q = -sys.maxsize,-sys.maxsize,sys.maxsize
    for key,val in v.items():
        if mx < val[0]:
            mxi,mx,q = key,val[0],val[1]
        if val[0] == mx and val[1] < q:
            mxi,mx,q = key,val[0],val[1]
    if mxi != -sys.maxsize: allname[mxi] += mx
    if mxi != -sys.maxsize: userprd[mxi].add(k)

ls = []
for k,v in allname.items():
    ls += [(k,v)]
ls.sort()

for item in ls:
    print("{}: ${} {} ".format(item[0],item[1],"" if item[1]==0 else "->"),end="")
    ls2 = []
    for val in userprd[item[0]]:
        ls2 += [val]
    ls2.sort()
    for val in ls2:
        print(val,end=" ")
    print()


# 4
# B b1 p4 4
# B b1 p3 3
# B b2 p1 1
# W b2 p1

# 9
# B b1 p1 2
# B b2 p1 2
# B b3 p1 2
# B b3 p2 99
# B b2 p2 2
# B b1 p2 2
# W b3 p2 
# B b3 p4 4
# B b1 p4 4
