inx = 0
walk = [(0,-1),(-1,0),(0,1),(1,0)]

def Mwalk(M,inx,row,col,D):
    n = len(M)
    while D>0:
        while 0<=row<n and 0<=col<n and M[row][col]==0:
            M[row][col] = D
            D -= 1
            row += walk[inx][0]
            col += walk[inx][1]
            if D==0:
                break
        row -= walk[inx][0]
        col -= walk[inx][1]
        inx = (inx+1)%len(walk)
        row += walk[inx][0]
        col += walk[inx][1]
    return M

def spiral_square(n):
    M = [[0]*n for i in range(n)]
    return Mwalk(M,0,n-1,n-1,n*n)

def print_square(S): 
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())

