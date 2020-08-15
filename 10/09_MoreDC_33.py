def tolist(o):
    ls = []
    for k,v in o.items():
        if v!=0: ls.append((v,k))
    return sorted(ls,key=lambda x:x[1],reverse=True)

def add_poly(p1, p2):
    o = {}
    for i in range(len(p1)):
        o[p1[i][1]] = p1[i][0]
    for i in range(len(p2)):
        if p2[i][1] in o:
            o[p2[i][1]] += p2[i][0]
        else:
            o[p2[i][1]] = p2[i][0]
    return tolist(o)

def mult_poly(p1, p2):
    o = {}
    for i in range(len(p1)):
        for j in range(len(p2)):
            v,k = p1[i][0]*p2[j][0],p1[i][1]+p2[j][1]
            if k in o: o[k] += v
            else: o[k] = v
    return tolist(o)

if __name__ == '__main__':
    for i in range(3):
        exec(input().strip())

# p1 = [(3,6),(2,4),(1,1),(-1,0)] 
# p2 = [(3,4),(-1,1)] 
# print(add_poly(p1, p2))

# p1 = [(3,6),(2,4)]
# p2 = [(1,4),(-1,2)] 
# print(mult_poly(p1, p2))