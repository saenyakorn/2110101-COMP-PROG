def error():
    print("error")
    exit()

s = input()
cha = ""
cnt = 0
s = s.upper()
encode_cha = []
encode_cnt = []
for i in s:
    if not i in ["A","T","C","G"]:
        error()
    if i != cha:
        encode_cha += [cha]
        encode_cnt += [cnt]
        cha = i
        cnt = 1
    else :
        cnt += 1
encode_cha = encode_cha[1:] + [cha]
encode_cnt = encode_cnt[1:] + [cnt]
for i in range(len(encode_cha)):
    print("{}{}".format(encode_cha[i],encode_cnt[i] if encode_cnt[i]!=1 else ""),end="")
print()