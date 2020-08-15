R = lambda c : "A" if c=="T" else ("T" if c=="A" else ("G" if c=="C" else ("C" if c=="G" else "X")))
l = ["A","T","G","C"]
dna = input().strip().upper()
cmd = input().strip().upper()
for c in dna:
    if not c in l:
        print("Invalid DNA")
        exit()
if cmd=="R":
    new_dna = []
    for c in dna:
        new_dna += [R(c)]
    new_dna = reversed(new_dna)
    for item in new_dna:
        print(item,end="")
    print()
elif cmd=="F":
    dic_key = ["A","T","G","C"]
    dic_val = [0,0,0,0]
    for c in dna:
        dic_val[dic_key.index(c)] += 1
    use = 0
    for i in range(len(dic_key)):
        print("{}{}={}".format(", " if use else "",dic_key[i],dic_val[i]),end="")
        use = 1
    print()
elif cmd=="D":
    inter = input().strip()
    inx = 0
    cnt = 0
    while dna.find(inter,inx)!=-1:
        cnt += 1
        inx = dna.find(inter,inx)+1
    print(cnt)