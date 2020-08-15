s = input().lower()
frq = {}
for c in s:
    if 'a' <= c <= 'z':
        if c in frq : frq[c] += 1
        else : frq.update({c:1}) 
ls = []
for k,v in frq.items():
    ls += [(k,v)]
ls.sort(key = lambda x : x[0])
ls.sort(key = lambda x : x[1],reverse=True)
for item in ls:
    print("{} -> {}".format(item[0],item[1]))