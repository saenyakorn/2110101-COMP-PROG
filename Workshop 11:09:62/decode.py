def error():
    print("error")
    exit()

s = input()
i = 0
cha = ""
output = ""
while i < len(s):
    cha = s[i]
    cnt = ""
    i += 1
    while i < len(s) :
        if "0" <= s[i] <= "9":
            cnt += s[i]
        else :
            break
        i += 1
    if i < len(s) and cha == s[i]:
        error()
    cnt = cnt if cnt!="" else "1"
    output += cha*int(cnt)
if len(output) > 50 :
    error()
print(output)