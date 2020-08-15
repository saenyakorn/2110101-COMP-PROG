def plusTime(t1,t2):
    m1,s1 = [int(e) for e in t1.split(':')]
    m2,s2 = [int(e) for e in t2.split(':')]
    return str(m1+m2+(s1+s2)//60)+':'+ ("0" if (s1+s2)%60<10 else "") +str((s1+s2)%60)
def intTime(t):
    m,s = [int(e) for e in t.split(':')]
    return m*60+s
def strTime(t):
    m,s = t//60,t%60
    return str(m)+':'+ ("0" if s<10 else "") +str(s)

dic = {}
for i in range(int(input())):
    sng,aut,sty,tim = [e.strip() for e in input().split(',')]
    if sty in dic:
        dic[sty] = plusTime(dic[sty],tim)
    else:
        dic[sty] = tim
ls = []
for k,v in dic.items():
    ls.append([k,intTime(v)])
ls.sort(key=lambda x: x[1],reverse=True)
for i in range(min(len(ls),3)):
    print("{} --> {}".format(ls[i][0],strTime(ls[i][1])))

# 9
# Shake It Off, Taylor Swift, Pop, 3:39
# Rolling In The Deep, Adele, Pop, 3:48 
# Chandelier, Sia, Pop, 3:36
# Roar, Katy Perry, Pop, 3:42
# Hotel California, Eagle, Rock, 6:30
# We Are the Champions, Queen, Rock, 2:59
# Hello Dolly, Louis Armstrong, Jazz, 2:27 
# Bohemian Rhapsody, Queen, Rock, 5:55
# Coward of the County, Kenny Rogers, Country, 4:02