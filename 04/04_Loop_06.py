n = int(input())
print("{}*".format(" "*(n-1)))
for i in range(2,n+1):
    print("{}*{}*".format(" "*(n-i),"*"*(2*i-3) if i==n else " "*(2*i-3)))