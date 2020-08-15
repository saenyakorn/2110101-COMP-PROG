group = ['A','B','C','Dog','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

def isInt(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def intersect(ls,req):
    o = []
    for i in range(len(ls)):
        chk = True
        for j in range(len(req)):
            if req[j]!="" and req[j]!=ls[i][j+1]:
                chk = False
                break
        if chk: o.append(ls[i])
    return sorted(o,key=lambda x:x[0])

if __name__ == '__main__':
    ls,o = [],[]
    for i in range(int(input())):
        nm,gp,yr,br = [e for e in input().split()]
        ls.append([nm,gp,yr,br])
    req = input().split()
    rgp,ryr,rbr = "","",""
    for i in range(len(req)):
        if isInt(req[i]): ryr = req[i]
        elif req[i] in group: rgp = req[i]
        else: rbr = req[i]
    o = intersect(ls,[rgp,ryr,rbr])
    if len(o)==0: print('Not Found')
    else:
        for i in range(len(o)):
            for j in range(len(o[i])):
                print(o[i][j],end=" ")
            print()

# 8
# Krit A 97 CP
# Oat A 98 CE
# Pim C 99 CP
# Pun C 97 CHE
# Jame Dog 100 CE
# Art C 97 CP
# Benz Dog 99 CP
# Mark C 100 CP
# CP C

# 8
# Krit A 97 CP
# Oat A 98 CE
# Pim C 99 CP
# Pun C 97 CHE
# Jame Dog 100 CE
# Art C 97 CP
# Benz Dog 99 CP
# Mark C 100 CP
# CP 97

# 8
# Krit A 97 CP
# Oat A 98 CE
# Pim C 99 CP
# Pun C 97 CHE
# Jame Dog 100 CE
# Art C 97 CP
# Benz Dog 99 CP
# Mark C 100 CP
# 100