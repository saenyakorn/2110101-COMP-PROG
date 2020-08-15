s = input().strip().split()
l = []
for x in s:
    if x[0] == "#":
        l += [x[1:]]
l = sorted(l)
for i in range(len(l)):
    print("{}{}".format(", " if i!=0 else "",l[i]),end="")
print()

#Python is a great language that you should learn now. #Coding #DataScience
 