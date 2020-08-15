def row_number(t, e):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == e: return i
    return -1
def flatten(t): 
    o = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            o += [t[i][j]] if t[i][j]!=0 else []
    return o
def inversions(x):
    inver = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] > x[j]: inver += 1
    return inver
def solvable(t):
    if len(t)%2==1 and inversions(flatten(t))%2==0:
        return True
    if len(t)%2==0 and inversions(flatten(t))%2 != row_number(t,0)%2:
        return True
    return False

if __name__ == '__main__':
    exec(input().strip())