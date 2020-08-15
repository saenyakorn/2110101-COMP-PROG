def read_matrix(): 
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split() 
        r = []
        for e in x:
            r.append( float(e) ) 
        m.append(r)
    return m
def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A
def mult(A, B):
    c = []
    for i in range(len(A)):
        s = [0]*(len(B[-1]))
        for j in range(len(B[-1])):
            for k in range(len(B)): 
                s[j] += A[i][k]*B[k][j]
        c .append(s)
    return c

if __name__ == '__main__':
    exec(input().strip())

# A=read_matrix();print(mult_c(0.5,A)) 
# 3
# 1 2
# 2 3
# 3 2

# A=read_matrix();B=read_matrix();print(mult(A,B))
# 3 
# 1 2 3 
# 1 1 1 
# 2 2 2 
# 3
# 1 2
# 2 3 
# 3 2