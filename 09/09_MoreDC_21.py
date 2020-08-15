def factor(n):
    o = []
    i = 2
    while n > 1:
        j = 0
        while n%i == 0:
            j += 1
            n //= i
        if j > 0: o += [[i,j]]
        i += 1
    return o
if __name__ == '__main__':
    exec(input().strip())
