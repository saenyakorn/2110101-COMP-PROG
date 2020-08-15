def rotate90(L):
    n = len(L)
    m = len(L[0])
    temp = ["" for e in range(m)]
    for i in range(m):
        c = ""
        for j in range(n):
            c += str(L[n-j-1][i])
        temp[i] = c
    return temp
def print_table(L):
    for t in L:
        print(t)
def main():
    cmd = input()
    n = int(input())
    size = 0
    l = ["" for e in range(n)]
    
    for i in range(n):
        s = input()
        size = size if i>0 else len(s)
        if len(s)!=size:
            return print("Invalid size")
        l[i] = s[::-1] if cmd=="flip" else s
    if cmd=="90":
        l = rotate90(l)
    if cmd=="180":
        l = rotate90(l)
        l = rotate90(l)
    print_table(l)
    
if __name__ == "__main__":
    main()