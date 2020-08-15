s = input().split()
cmd = input()
n = len(s)
for c in cmd:
    if c=="C":
        s = s[n//2:] + s[:n//2]
    elif c=="S":
        a = s[n//2:]
        b = s[:n//2]
        s = []
        for i in range(n//2):
            s += [b[i]] + [a[i]]
for c in s:
    print(c ,end=" ")
print()