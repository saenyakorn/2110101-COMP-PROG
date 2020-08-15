def is_odd(n) :
    return True if n%2 else False
def has_odds(ls):
    for x in ls:
        if is_odd(x) : return True
    return False
def all_odds(ls):
    for x in ls:
        if not is_odd(x) : return False
    return True
def no_odds(ls):
    for x in ls :
        if is_odd(x) : return False
    return True
def get_odds(ls):
    o = []
    for x in ls :
        o += [x] if is_odd(x) else []
    return o
def next_odd(ls,inx) :
    for i in range(inx,len(ls)):
        if is_odd(ls[i]): return i
    return -1
def zip_odds(lsA,lsB) :
    inxA,inxB = 0,0
    o = []
    while inxA != -1 or inxB != -1 :
        if inxA != -1:
            inxA = next_odd(lsA,inxA)
            o += [lsA[inxA]] if inxA != -1 else []
            inxA += 1 if inxA != -1 else 0
        if inxB != -1:
            inxB = next_odd(lsB,inxB)
            o += [lsB[inxB]] if inxB != -1 else []
            inxB += 1 if inxB != -1 else 0
    return o
if __name__ == '__main__' :
    exec(input().strip())