import numpy as np

n,m = [int(e) for e in input().split()]

x = []
for i in range(n):
    x.append([int(e) for e in input().split()])
x = np.array(x).reshape((n,m))
y = np.array([int(e) for e in input().split()]).reshape((1,n))
w = np.array([int(e) for e in input().split()]).reshape((1,m))
xT = x.T
result = 2*(xT.dot( (w.dot(xT)-y).T )) / n
for i in range(result.shape[0]):
    print("%.3f"%result[i][0])

# 3 5
# 1 1 2 1 2
# 1 2 4 2 4 
# 1 6 3 6 3 
# 3 5 4 
# 1 2 3 4 5

# 3 3 
# 1 3 8
# 1 5 4
# 1 6 7
# 4 4 2 
# 1 8 4