cmd = input()
if "str2RLE" == cmd:
    s = input()
    c = ""
    l = []
    cnt = []
    n = 0
    for x in s:
        if c != x:
            l += [c]
            cnt += [n]
            c = x
            n = 1
        else :
            n += 1
    l += [c]
    cnt += [n]
    for i in range(1,len(l)):
        print("{} {}".format(l[i],cnt[i]),end=" ")
    print()
elif "RLE2str" == cmd:
    s = input().split()
    for i in range(0,len(s),2):
        for j in range(int(s[i+1])):
            print(s[i],end="")
    print()
else:
    print("Error")