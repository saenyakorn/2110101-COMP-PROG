dic = {}
for i in range(int(input())):
    k,v = [e for e in input().split()]
    dic.update({k:(int(v),0)})
for i in range(int(input())):
    k,v = [e for e in input().split()]
    if k in dic: dic[k] = (dic[k][0],dic[k][1] + int(v))
ls,top = [],[]
for k,v in dic.items():
    ls += [(k,v[0]*v[1])]
ls.sort(key = lambda x : x[0])
ls.sort(key = lambda x : x[1],reverse=True)
total = 0.0
temp = ls[0][1]
if temp == 0:
    print("No ice cream sales");
    exit()
for item in ls:
    total += item[1]
    top += [item[0]] if item[1]==temp else []
print("Total ice cream sales:",total)
print("Top sales: ",end="")
for item in top:
    print("{}{}".format("" if item==top[0] else ", ",item),end="")
print()
