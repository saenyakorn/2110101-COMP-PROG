name = ["Robert","William","James","John","Margaret","Edward","Sarah","Andrew","Anthony","Deborah"]
nick = ["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
t1 = {k:v for k,v in zip(name,nick)}
t2 = {k:v for k,v in zip(nick,name)}

n = int(input())
for i in range(n):
    s = input()
    print("{}".format(t1[s] if s in t1 else (t2[s] if s in t2 else "Not found")))