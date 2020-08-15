d,m,y = [int(e) for e in input().split()]
month = [31,28,31,30,31,30,31,31,30,31,30,31]
f = lambda a : a-543
month[1] = 29 if (f(y)%400==0) or ( f(y)%4==0 and f(y)%100 ) else 28

d += 15 
if d > month[m-1] : 
    d -= month[m-1]
    m += 1
if m > 12 :
    y += 1
    m = 1
print(d,m,y,sep="/")
