brs = {}
for i in range(int(input())):
    br,n = input().split()
    brs[br] = int(n)

ls = []
for i in range(int(input())):
    inp = input().split()
    ls.append(inp)
    ls[i][1] = float(ls[i][1])
ls.sort(key=lambda x:x[1],reverse=True)

o = []
for i in range(len(ls)):
    itrs = ls[i][2:]
    for j in range(len(itrs)):
        if brs[itrs[j]] > 0:
            brs[itrs[j]] -= 1
            o += [(ls[i][0],itrs[j])]
            break
o.sort(key=lambda x:x[0])
for i in range(len(o)):
    print(o[i][0],o[i][1])

# 5
# CP 1
# ME 2
# PE 1
# CHE 1
# MT 3
# 6
# 59301234521 23.6 PE CP MT CHE 
# 59300799921 44.5 ME CP CHE PE 
# 59300081621 37 PE CHE MT CP 
# 59300653521 61.2 PE MT CP ME 
# 59300002121 19.4 CHE CP ME CP 
# 59300048721 7 ME CP CHE MT 