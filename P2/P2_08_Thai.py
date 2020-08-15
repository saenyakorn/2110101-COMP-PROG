number = ['soon','neung','song','sam','si','ha','hok','chet','paet','kao','sip',\
    'et','yi','roi','pun']

def to_Thai(n):
    if n <= 10:
        return number[n]
    elif n == 11:
        return number[10] + ' ' + number[11]
    elif 11 < n < 20:
        return number[10] + ' ' + number[n%10]
    elif n == 20:
        return number[12] + ' ' + number[10]
    elif n == 21:
        return number[12] + ' ' + number[10] + ' ' + number[11]
    elif 21 < n < 30:
        return number[12] + ' ' + number[10] + ' ' + number[n%10]
    elif n < 100 and n%10 == 0:
        return number[n//10] + ' ' + number[10]
    elif n < 100 and n%10 == 1:
        return number[n//10] + ' ' + number[10] + ' ' + number[11]
    elif n < 100:
        return number[n//10] + ' ' + number[10] + ' ' + number[n%10]
    elif 100 <= n <= 999:
        if n%100 == 0:
            return number[n//100] + ' ' + number[13]
        elif n%100 == 1:
            return number[n//100] + ' ' + number[13] + ' ' + number[11]
        else:
            return number[n//100] + ' ' + number[13] + ' ' + to_Thai(n%100)
    elif 1000 <= n <= 9999:
        if n%1000 == 0:
            return number[n//1000] + ' ' + number[14]
        elif n%1000 == 1:
            return number[n//1000] + ' ' + number[14] + ' ' + number[11]
        else:
            return number[n//1000] + ' ' + number[14] + ' ' + to_Thai(n%1000)

if __name__ == '__main__':
    #for i in range(1020):
    #   print(i,to_Thai(i))
    exec(input().strip())