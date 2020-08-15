import math

def CountDay(d,m,y,h):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    f = lambda a : a-543
    month[1] = 29 if (f(y)%400==0) or (f(y)%4==0 and f(y)%100) else 28
    day = 0
    if h==0: # now to end
        day = month[m-1]-d+1
        while m < len(month):
            day += month[m]
            m += 1
    else: # start to now
        day = d-1
        for i in range(m-1):
            day += month[i]
    return day

bd, bm, by, d, m, y = [int(e) for e in input().split()]
Before = CountDay(bd,bm,by,0)
#print(Before)
After = CountDay(d,m,y,1)
#print(After)
Until = (y-by-1)*365
total = Before + Until + After
c = 2*math.pi*total
a = math.sin(c/23)
b = math.sin(c/28)
c = math.sin(c/33)
print("{} {:.2f} {:.2f} {:.2f}".format(total,a,b,c))
