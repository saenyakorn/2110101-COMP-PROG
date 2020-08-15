def error():
    print("error")
    exit()
    return 0

try:
    sl = [int(e) for e in input().replace(" ","").split(",")]
    for i in sl:
        if not 0 <= i <= 10:
            error()
    i = 0
    r = 0
    score = 0
    while i < len(sl):
        if (not 0 <= sl[i] <= 10) or r>=5:
            error()
        if r == 4:
            score += sl[i]
            score += sl[i+1]
            score += (sl[i+2] if sl[i]==10 or sl[i]+sl[i+1]==10 else error())  
            if sl[i]==10 and sl[i+1]==10 and sl[i+2] > 10:
                error()
            if sl[i]==10 and sl[i+1]!=10 and sl[i+1] + sl[i+2] > 10:
                error()
            if sl[i]!=10 and sl[i]+sl[i+1] > 10:
                error()
            if sl[i]!=10 and sl[i]+sl[i+1]>10:
                error()
            if i+2 < len(sl) and i+3 < len(sl):
                error()
            i += 3
            r += 1
        elif sl[i]==10:
            score += sl[i] 
            score += sl[i+1]
            score += sl[i+2]
            i += 1
            r += 1 
        else:
            score += sl[i]
            score += sl[i+1]
            score += sl[i+2] if sl[i]+sl[i+1]==10 else 0
            if (sl[i]+sl[i+1] > 10) or (sl[i]+sl[i+1]==10 and sl[i+2] > 10):
                error()
            i += 2
            r += 1
    print(score)
except:
    error()