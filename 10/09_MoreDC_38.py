station = {}

while True:
    inp = input().split()
    if len(inp)==1: break
    if inp[0] in station: station[inp[0]].add(inp[1])
    else: station[inp[0]] = {inp[1]}
    if inp[1] in station: station[inp[1]].add(inp[0])
    else: station[inp[1]] = {inp[0]}

if inp[0] not in station:
    print(inp[0])
    exit()

o = set()
Q = [(inp[0],0)]
while len(Q) > 0:
    u,inx = Q.pop(0)
    if inx <= 2:
        o.add(u)
        for item in station[u]:
            Q.append((item,inx+1))
ls = []
for item in o:
    ls += [item]
ls.sort()
for i in range(len(ls)):
    print(ls[i])

# Siam ChitLom
# ChitLom PhloenChit
# PhloenChit Nana
# Siam NationalStadium
# Ratchadamri Siam
# Siam PhayaThai
# Ratchadamri SalaDaeng
# ThongLo Ekkamai
# Ekkamai ThongLo
# Siam