doc = {}
doccnt = {}
for i in range(int(input().strip())):
    docname = input().strip()
    doc[docname] = {}
    doccnt[docname] = 0
    for item in input().split():
        word = item.strip()
        doc[docname][word] = doc[docname][word] + 1 if word in doc[docname] else 1
        doccnt[docname] += 1

while True:
    word = input().strip()
    if word=='-1':
        break
    mx,mxi = -1,-1
    for k,v in doc.items():
        scr = -1
        if word in v:
            scr = v[word] / doccnt[k] / len(v)
        if scr > mx:
            mx = scr
            mxi = k
    print(mxi if mx >= 0 else "NOT FOUND")

# 3
# PPAP
# I HAVE A PEN I HAVE AN APPLE AH PINEAPPLE PEN
# MYAPPLE
# APPLE WATCH MACBOOK AIR IPOD APPLE ORANGE
# GOOGLE
# GOOGLE MY WATCH AND GET MACBOOK AIR AND FREE I PHONE WATCH YOUTUBE