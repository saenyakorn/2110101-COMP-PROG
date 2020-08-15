import numpy as np

def remake(tab):
    ever = set()
    cal = 0
    pos = 0
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]):
            if tab[i,j] != 'x' and tab[i,j] not in ever:
                ever.add(tab[i,j])
                cal += int(tab[i,j])
            if tab[i,j] == 'x':
                pos = (i,j)
    tab[pos] = cal//len(ever)
    return tab

def hasX(tab):
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]):
            if tab[i,j] == 'x':
                return (i,j)
    return (-1,-1)

n = int(input())
tab = np.array(input().split()).reshape((n,n))

for i in range(n-1):
    for j in range(n-1):
        if hasX(tab[i:i+2,j:j+2]) != (-1,-1):
            tab[i:i+2,j:j+2] = remake(tab[i:i+2,j:j+2])

for i in range(n):
    print(' '.join(tab[i]))

# 2 
# 127 127 97 x

# 5 
# x 192 84 138 138 97 84 x x 138 10 x x 252 138 255 10 10 17 252 121 10 185 192 255 