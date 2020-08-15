n = int(input())
l = [n]
while n > 1:
    n = 3*n+1 if n%2 else n//2
    l.append(n)
sym = False
for e in (l[-15:] if len(l) > 15 else l):
    print("{}{}".format("->" if sym else "",e),end="")
    sym = True
print()