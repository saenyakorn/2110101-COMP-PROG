L = list(float(x) for x in input().split())
L.sort()
print(round((L[1]+L[2])/2,2))