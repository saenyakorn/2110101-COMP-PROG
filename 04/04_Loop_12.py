import sys

n = int(input())
L = []
for i in range(n):
    x,y = input().split()
    L.append((int(x),int(y)))
cmd = input()
mx = -sys.maxsize
mn = sys.maxsize
for i in range(n):
    mn = min(mn,L[i][i%2] if cmd == "Zig-Zag" else L[i][(i+1)%2])
    mx = max(mx,L[i][(i+1)%2] if cmd == "Zig-Zag" else L[i][i%2])
print(mn,mx)