s = input()
key = ["A","B+","B","C+","C","D+","D","F"]
val = [e for e in range(len(key))]
stu = []
while s != "q":
    k,v = s.split()
    stu.append((k,v))
    s = input()
s = input().split()
for e in stu:
    if e[0] in s:
        i = key.index(e[1])
        print(e[0],e[1] if e[1]=="A" else key[val[i]-1])
    else : 
        print(e[0],e[1])