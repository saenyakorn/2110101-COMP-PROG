s = input()
digit = [1 for i in range(0,10)]
for c in s:
    if "0" <= c <= "9":
        digit[int(c)] = 0
comma = False
for i in range(10):
    if digit[i]:
        print("{}{}".format("," if comma else "",i),end="")
        comma = True
print("{}".format("" if comma else "None"))