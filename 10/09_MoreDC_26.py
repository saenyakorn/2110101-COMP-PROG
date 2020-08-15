dic = {}
for i in range(int(input())):
    ID,key = [e.strip() for e in input().split(':')]
    ls = [e.strip() for e in key.split(',')]
    dic[ID] = [ls,i]

o = set()
terminal = input()
if terminal in dic:
    for tr in dic[terminal][0]:
        for k,v in dic.items():
            if k != terminal and tr in v[0]: o.add((k,v[1]))
    if len(o)==0:
        print('Not Found')
    else:
        ls = []
        for item in o:
            ls.append(item)
        ls.sort(key=lambda x:x[1])
        for item in ls:
            print(item[0])
    
else:
    print('Not Found')

# 2
# 51234621: A, B, D, E, F 
# 427613829: B, D, G, H, I 
# 38216542: Z, B, D, J 
# 423212822: AA, B1, C3, D 
# 4126548: J, Z3 
# 98871973331: Q, M, N 
# 4126548
