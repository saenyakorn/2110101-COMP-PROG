p = input()
p = float(p)
k = 1
t = 1.0
while 1.0-t < p :
    k += 1
    t = (t*(365-(float(k)-1)))/365
    if 1.0-t >= p :
        break
print(k)
