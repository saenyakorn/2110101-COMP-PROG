def readMe(filename):
    f = open(filename,'r')
    dic = {}
    for line in f:
        a,b = line.strip('\n').split(',')
        dic[a] = b
    f.close()
    return dic

if __name__ == '__main__':
    cu = readMe(input().strip())
    th = readMe(input().strip())
    f = open(input().strip())
    for line in f:
        f,b = line.strip('\n').split(',')
        if f in cu and b in th:
            print('{},{}'.format(cu[f],th[b]))
        else:
            print('record error')

