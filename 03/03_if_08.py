d = int(input())
m = int(input())
y = int(input())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
f = lambda a : a-543
month[1] = 29 if (f(y)%400==0) or ( f(y)%4==0 and f(y)%100 ) else 28

day = d
for i in range(0,m-1):
    day += month[i]
print(day)
