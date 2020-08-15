win,lose = set(),set()
for i in range(int(input())):
    w,l = input().split()
    win.add(w)
    lose.add(l)
for item in lose:
    if item in win:
        win.remove(item)
ls = []
for item in win:
    ls.append(item)
print(sorted(ls))

# 5
# Chelsea Liverpool
# ManU Liverpool
# Liverpool ManU
# Chelsea Arsenal
# Everton ManCity

# 4
# Arsenal ManCity
# Arsenal Everton
# Arsenal Tottenham
# ManCity Arsenal