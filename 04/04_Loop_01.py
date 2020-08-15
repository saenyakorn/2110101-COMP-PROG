s = 0.0
mem = 0
while True :
    cmd = input()
    if cmd == 'q':
        break
    mem += 1
    s += float(cmd)
print("{}".format(round(s/mem,2) if mem>0 else "No Data"))