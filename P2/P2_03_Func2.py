def convex_polygon_area(p):
    s = 0
    for i in range(len(p)):
        a,b = i%len(p),(i+1)%len(p)
        s += p[a][0]*p[b][1] - p[a][1]*p[b][0]
    return s/2 if s>0 else -s/2
def is_heterogram(s):
    dic = {}
    for i in range(26):
        dic[chr(ord('a')+i)] = 0
    for c in s.lower():
        if 'a' <= c <= 'z': 
            dic[c] += 1
            if dic[c] > 1: return False
    return True
def replace_ignorecase(s, a, b):
    inx = 0
    o = ''
    while inx < len(s):
        All = 1
        for i in range(inx,inx+len(a)):
            if i < len(s) : All = All and (s[i].lower()==a[i-inx].lower())
            else : All = 0
        if All:
            o += b
            inx += len(a)
        else : 
            o += s[inx]
            inx += 1
    return o
def top3(votes):
    ls,win = [],[]
    for key,val in votes.items():
        ls += [(val,key)]
    ls.sort(key= lambda x: x[1])
    ls.sort(key= lambda x: x[0], reverse=True)
    for i in range(min(len(ls),3)):
        win += [ls[i][1]]
    return win

if __name__ == '__main__':
    for k in range(2):
        exec(input().strip())