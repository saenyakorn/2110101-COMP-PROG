mname = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
mday = [31,28,31,30,31,30,31,31,30,31,30,31]
def read_date():
    s = input().split()
    return [int(s[0]),mname.index(s[1])+1,int(s[2])]
def zodiac(d,m):
    z = ""
    if   d >= 22 and m==3  or d <=21 and m==4  : z = "Aries"
    elif d >= 22 and m==4  or d <=21 and m==5  : z = "Taurus"
    elif d >= 22 and m==5  or d <=21 and m==6  : z = "Gemini"
    elif d >= 22 and m==6  or d <=21 and m==7  : z = "Cancer"
    elif d >= 22 and m==7  or d <=21 and m==8  : z = "Leo"
    elif d >= 22 and m==8  or d <=21 and m==9  : z = "Virgo"
    elif d >= 22 and m==9  or d <=21 and m==10 : z = "Libra"
    elif d >= 22 and m==10 or d <=21 and m==11 : z = "Scorpio"
    elif d >= 22 and m==11 or d <=21 and m==12 : z = "Sagittarius"
    elif d >= 22 and m==12 or d <=20 and m==1  : z = "Capricorn"
    elif d >= 21 and m==1  or d <=20 and m==2  : z = "Aquarius"
    elif d >= 21 and m==2  or d <=21 and m==3  : z = "Pisces"
    return z
def days_in_feb(y):
    return 29 if y % 400 == 0 or y % 100 != 0 and y%4 == 0 else 28
def days_in_month(m,y):
    return mday[m-1] if m!=2 else days_in_feb(y)
def day_from_year(d,m,y):
    for i in range(1,m):
        d += days_in_month(i,y)
    return d
def day_to_year(d,m,y):
    d = -d
    for i in range(m,13):
        d += days_in_month(i,y)
    return d
def days_in_between(d1,m1,y1,d2,m2,y2):
    x = day_from_year(d2,m2,y2)-1 + day_to_year(d1,m1,y1)
    for i in range(y1+1,y2):
        x += 365 if days_in_feb(i)==28 else 366
    return x

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1),zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))
if __name__ == "__main__":
    exec(input().strip())