import sys
fname,yr = [e for e in input().split()]
f = open(fname,"r")
dat = f.read().split()
stuid = []
score = []
for i in range(0,len(dat),2):
    stuid.append(dat[i])
    score.append(float(dat[i+1]))
yr = yr[-2:]
mn = sys.maxsize
mx = -sys.maxsize
sm = 0.0
n = 0
for i in range(len(stuid)):
    if stuid[i][:2] == yr:
        mn = min(mn,score[i])
        mx = max(mx,score[i])
        sm += score[i]
        n += 1
print("No data" if n==0 else "{} {} {}".format(mn,mx,sm/n))