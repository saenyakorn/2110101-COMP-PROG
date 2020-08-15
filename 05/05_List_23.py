import math as m
import operator as op

n = int(input())
p = []
for i in range(n):
    x,y = [float(e) for e in input().split()]
    p.append((x,y,i+1))
sp = sorted(p,key=lambda x: m.sqrt(x[1]*x[1] + x[0]*x[0]))
print("#{}: ({}, {})".format(sp[2][2],sp[2][0],sp[2][1]))