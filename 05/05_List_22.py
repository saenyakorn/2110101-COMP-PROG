s = input()
key = ["A","B+","B","C+","C","D+","D","F"]
val = [e for e in range(len(key))]
gton = {k:v for k,v in zip(key,val)}
ntog = {k:v for k,v in zip(val,key)}
stu = {}
while s != "q":
    k,v = s.split()
    stu.update({k:gton[v]})
    s = input()
s = input().split()
for e in s:
    stu[e] = stu[e]-1 if stu[e]>0 else stu[e]
for e in sorted(stu.keys()):
    print(e,ntog[stu[e]])