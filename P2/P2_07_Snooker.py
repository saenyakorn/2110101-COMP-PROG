ls = [0,0]
rn = 0
score = {'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7,'X':0}
while True:
    s = input().strip()
    p = int(s[0])-1
    if len(s) == 3:
        ls[p] += score[s[1]] + score[s[2]]
        rn += 1 if s[2]=='X' else 0
    if len(s) == 2:
        ls[p] += score[s[1]]
        rn += 1 if s[1]=='X' else 0
    if s[1]=='K': break
print(ls[0],ls[1])
if ls[0] == ls[1]: print("Tie")
else: print("Player {} wins".format(1 if ls[0] > ls[1] else 2))