m = ["January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"]

a,b,c = input().split('/')
print("{} {}, {}".format(m[int(b)-1],a,c))