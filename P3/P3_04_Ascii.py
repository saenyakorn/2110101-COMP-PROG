def is_all_row_space(M,col):
    return all([M[i][col]=='.' for i in range(len(M))])
def is_all_col_space(M,row):
    return all([M[row][j]=='.' for j in range(len(M[row]))])
def display(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j],end="")
        print()

def LSTRIP(M):
    all_row = []
    for i in range(len(M[0])):
        all_row.append(is_all_row_space(M,i))
    left = 0
    while left<len(all_row) and all_row[left]: 
        left+=1
    new_M = []
    for i in range(len(M)):
        new_M.append(M[i][left:])
    return new_M
def RSTRIP(M):
    all_row = []
    for i in range(len(M[0])):
        all_row.append(is_all_row_space(M,i))
    right = len(all_row)-1
    while right>=0 and all_row[right]: 
        right-=1
    right+=1
    new_M = []
    for i in range(len(M)):
        new_M.append(M[i][:right])
    return new_M
def STRIP(M):
    return LSTRIP(RSTRIP(M))
def STRIP_ALL(M):
    M = STRIP(M)
    new_M = []
    all_row = []
    for i in range(len(M[0])):
        all_row.append(is_all_row_space(M,i))
    for i in range(len(M)):
        o = ""
        for j in range(len(M[i])):
            if not all_row[j]: o += M[i][j]
        new_M.append(o)
    return new_M
if __name__ == '__main__':
    fname = input().strip()
    mode = input().strip()
    f = open(fname,'r')
    M = []
    for line in f:
        M.append(line.strip('\n').strip())
    if mode=='LSTRIP':
        display(LSTRIP(M))
    elif mode=='RSTRIP':
        display(RSTRIP(M))
    elif mode=='STRIP':
        display(STRIP(M))
    elif mode=='STRIP_ALL':
        display(STRIP_ALL(M))
    else:
        print("Invalid command")