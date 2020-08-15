A,B = input().strip(),input().strip()
a,b = "",""
dicA,dicB = {},{}

for c in A.lower():
    a += c if 'a'<=c<='z' else ""
for c in B.lower():
    b += c if 'a'<=c<='z' else ""

for c in a:
    if c in dicA: dicA[c] += 1
    else: dicA[c] = 1
for c in b:
    if c in dicB: dicB[c] += 1
    else: dicB[c] = 1

print(A)
lsA = []
for key,val in dicA.items():
    if key in dicB and dicA[key]-dicB[key] > 0: lsA += [(key,dicA[key]-dicB[key])]
    elif key not in dicB: lsA += [(key,dicA[key])]

if len(lsA) > 0:
    lsA.sort(key=lambda x:x[0])
    for item in lsA:
        if item[1] > 0: print('- remove',item[1],item[0] if item[1]==1 else item[0]+"'s")
else: print(' - None')

print(B)
lsB = []
for key,val in dicB.items():
    if key in dicA and dicB[key]-dicA[key] != 0: lsB += [(key,dicB[key]-dicA[key])]
    elif key not in dicA: lsB += [(key,dicB[key])]

if len(lsB) > 0:
    lsB.sort(key=lambda x:x[0])
    for item in lsB:
        if item[1] > 0: print(' - remove',item[1],item[0] if item[1]==1 else item[0]+"'s")
else: print(' - None')



