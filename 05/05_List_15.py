l = [int(a) for a in input().split()]
l.sort()
o = []
n = 0
num = l[0]+1
for e in l:
    if num != e:
        o.append(e)
        n += 1
        num = e
print(n)
print("{}".format(o[:10] if n>10 else o))