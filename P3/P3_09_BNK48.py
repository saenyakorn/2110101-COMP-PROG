cmd = ""
user = {} # to find kamioshi
idolname = {} # to find freq kamioshi
idolscr= {} # to find sum score
freq = {} # to find freq vote
while True:
    cmd = input().strip().split()
    if cmd[0] in ['1','2','3']:
        break
    nm,idol,scr = cmd[0],cmd[1],int(cmd[2])
    if nm in user: 
        if idol in user[nm]: user[nm][idol] += scr
        else: user[nm].update({idol:scr})
    else: user[nm] = {idol:scr}
    idolscr[idol] = idolscr[idol] + scr if idol in idolscr else scr
    if idol in freq: freq[idol].add(nm)
    else: freq[idol] = {nm}
    idolname[idol] = 0

for k,v in user.items():
    d = [(val,key) for key,val in v.items()]
    d = sorted(sorted(d,key=lambda x:x[1]),key=lambda x:x[0],reverse=True)
    idolname[d[0][1]] += 1

ls = []
if cmd[0] == '1':
    ls += [(k,v) for k,v in idolscr.items()]
    ls = sorted(sorted(ls,key=lambda x:x[0]),key=lambda x:x[1],reverse=True)
    o = [item[0] for item in ls]
    print(', '.join(o if len(o) < 3 else o[:3]))

if cmd[0] == '2':
    ls = [(k,len(v)) for k,v in freq.items()]
    ls = sorted(sorted(ls,key=lambda x:x[0]),key=lambda x:x[1],reverse=True)
    o = [item[0] for item in ls]
    print(', '.join(o if len(o) < 3 else o[:3]))

if cmd[0] == '3':
    ls = [(k,v) for k,v in idolname.items()]
    ls = sorted(sorted(ls,key=lambda x:x[0]),key=lambda x:x[1],reverse=True)
    o = [item[0] for item in ls]
    print(', '.join(o if len(o) < 3 else o[:3]))
 
 
# SOMCHAI CHERPRANG 10 
# SOMCHAI NATHERINE 5 
# PRABHAS JENNIS 3 
# SOMCHAI CHERPRANG 4 
# DUANGDAO TURTLE 1 
# EKAPOL TURTLE 1
# SETHA TURTLE 1 
# CHAIRAT TURTLE 1 
# JENNIS JENNIS 10 
# PRABHAS JANE 8
# MANA CHERPRANG 2 
# MANEE CHERPRANG 1 
# CHUJAI TURTLE 1
# PITI JENNIS 1
# PITI JANE 1
# VEERA CHERPRANG 1
# PITI DALO 1

# SOMCHAI AL 1
# SOMCHAI AB 1
# SOMCHAI BA 1
# SOMCHAI AA 1