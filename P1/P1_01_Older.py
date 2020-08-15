a = input().split();
b = input().split();
a[2] = a[2][:-1]
b[2] = b[2][:-1]
m = ["January","February","March","April","May","June","July","August","September","October","November","December"]
if a[3]!=b[3]:
    print("{}".format(a[0] if int(a[3]) < int(b[3]) else b[0]))
else :
    if m.index(a[1])!=m.index(b[1]):
        print("{}".format(a[0] if m.index(a[1]) < m.index(b[1]) else b[0]))
    else :
        print("{} {}".format(a[0] if int(a[2]) <= int(b[2]) else b[0],b[0] if int(a[2]) == int(b[2]) else ""))