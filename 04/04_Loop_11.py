s = input()
ap = ''
cn = 0
L = []
for x in s:
    if ap != x:
        L.append((ap,cn))
        cn = 1
        ap = x
    else : 
        cn += 1
L.append((ap,cn))
for i in range(1,len(L)):
    print(L[i][0] + " " + str(L[i][1]) ,end=' ')