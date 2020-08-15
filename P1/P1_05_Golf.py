import math as m
tpar = 0
tstk = 0
treb = 0
for i in range(9):
    par,stk,chc = [int(e) for e in input().split()]
    reb = min(par+2,stk)
    tpar += par
    tstk += stk
    treb += reb if chc else 0
toor = m.floor(0.8*(1.5*treb-tpar))
total = tstk - toor
print(tstk)
print(toor)
print(total)