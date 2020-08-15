def getPattern(pattern):
    dic = {}
    j,k = 0,0
    while True:
        k = pattern.find('[',j+1)
        if k == -1: break
        c = pattern[j+1]
        dic[c] = pattern[j+3:k]
        dic[dic[c]] = c
        j = k
    return dic

fileName = input().strip()
f = open(fileName,'r')

Type = f.readline().strip()
if Type not in ['T2M','M2T']:
    print('Invalid code')
    exit()

Pattern = f.readline().strip()
dic = getPattern(Pattern)

for line in f:
    if Type == 'T2M':
        s,chk = '',True
        for c in line.strip():
            if c in dic: s += dic[c] + ' '
            else: chk = False
        print(s if chk else ('Invalid : ' + line.strip()))
    elif Type == 'M2T':
        s,chk,t = '',True,line.strip().split()
        for item in t:
            if item in dic: s += dic[item]
            else: chk = False
        print(s if chk else ('Invalid : ' + line.strip()))

