numq = 0
cusn = 0
runq = 0
sumt = 0.0
cusl = []
cust = []
for i in range(int(input())):
    cmd = input()
    if "reset" in cmd:
        cmd,n = cmd.split()
        numq = int(n)
        runq = 0
    elif "new" in cmd:
        cmd,t = cmd.split()
        cusl.append(numq)
        cust.append(int(t))
        print("ticket",numq)
        numq += 1
    elif "next" in cmd:
        print("call",cusl[runq])
        runq += 1
    elif "order" in cmd:
        cmd,t = cmd.split()
        print("qtime",cusl[runq-1],int(t)-cust[runq-1])
        sumt += float(t)-cust[runq-1]
        cusn += 1
    elif "avg_qtime" in cmd:
        print("avg_qtime",round(sumt/cusn,4))

