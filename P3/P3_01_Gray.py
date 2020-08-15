def gray_code(n):
    code = ['0','1']
    for i in range(n-1):
        size = len(code)
        code += reversed(code)
        for j in range(size):
            code[j] = '0' + code[j]
        for j in range(size):
            code[size+j] = '1' + code[size+j]
    return code

def main():
    n = int(input())
    k = int(input())
    if n < 0 or k < 1:
        print('Invalid {}{}{}'.format("n " if n<1 else "","and " if n<1 and k<1 else "","k" if k<1 else ""))
        return 0
    ls = gray_code(n)
    for i in range(1,k+1):
        m = n if i<10 else n-1
        m = m if i!=k else m-1
        print(str(i) + "-"*m,end="")
    print()
    for i in range(len(ls)):
        print(ls[i],end="," if i%k!=k-1 and i!=len(ls)-1 else "\n")

if __name__ == '__main__':
    main()