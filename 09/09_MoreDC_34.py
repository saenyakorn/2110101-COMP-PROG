def pattern1(nrows, ncols):
    o,r = [],1
    for i in range(nrows):
        o.append([])
        for j in range(ncols):
            o[i].append(r)
            r += 1
    return o
def pattern2(nrows, ncols):
    o = []
    for i in range(nrows):
        o.append([])
        r = i+1
        for j in range(ncols):
            o[i].append(r)
            r += nrows
    return o
def pattern3(N):
    o,r = [],1
    for i in range(N):
        o.append([])
        for j in range(i):
            o[i].append(0)
        for j in range(N-i):
            o[i].append(r)
            r += 1
    return o
def pattern4(N):
    o,r = [],1
    for i in range(N):
        o.append([])
        for j in range(N):
            o[i].append(0)
    for j in range(N):
        for i in range(j+1):
            o[j-i][j] = r
            r += 1
    return o
def pattern5(N):
    o,r = [],1
    for i in range(N):
        o.append([])
        for j in range(N):
            o[i].append(0)
    for j in range(N):
        for i in range(N-j):
            o[i][i+j] = r
            r += 1
    return o
def pattern6(N):
    o,r = [],1
    for i in range(N):
        o.append([])
        for j in range(N):
            o[i].append(0)
    for j in range(N):
        if j%2==0:
            for i in range(N-j):
                o[i][i+j] = r
                r += 1
        else:
            for i in range(N-j):
                o[N-j-i-1][N-i-1] = r
                r += 1
    return o

if __name__ == '__main__':
    exec(input().strip())