dic = {}
i = 0
while True:
    inp = input().strip()
    if inp == 'q': break
    nm,ty = [e.strip() for e in inp.split(',')]
    if ty in dic: dic[ty][0].append(nm)
    else: dic[ty] = [[nm],i]
    i += 1
ls = []
for k,v in dic.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1][1])
for i in range(len(ls)):
    print("{}: ".format(ls[i][0]),end="")
    for j in range(len(ls[i][1][0])):
        print("{}{}".format(", " if j!=0 else "",ls[i][1][0][j]),end="")
    print()

# Ted, bear 
# Pongo, dog
# Fozzie, bear
# Winnie-the-Pooh, bear
# Nana, dog
# Hello Kitty, cat
# Scooby Doo, dog
# Garfield, cat
# Yogi, bear
# Tom, cat 
# Sylvester, cat
# q