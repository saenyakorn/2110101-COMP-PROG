import math

n = int(input())
p = math.pi
e = math.e
po1 = -n+1/(12*n+1)
po2 = -n+1/(12*n)
lower = math.sqrt(2*p) * (n**(n+0.5)) * (e**po1)
upper = math.sqrt(2*p) * (n**(n+0.5)) * (e**po2)

print(lower)
print(upper)