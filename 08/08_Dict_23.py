tel = {}
for i in range(int(input())):
    n,s,t = [e for e in input().split()]
    tel.update({n+" "+s:t})
    tel.update({t:n+" "+s})
for i in range(int(input())):
    k = input()
    if k in tel: print("{} --> {}".format(k,tel[k]))
    else: print("{} --> Not found".format(k))