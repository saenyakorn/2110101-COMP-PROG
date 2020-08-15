l = []
while True:
    s = input()
    if s == "end":
        break
    new_s = ""
    for c in s:
        if "A" <= c <= "Z" :
            new_s += chr((ord(c)+13)%(ord("Z")+1) + ord("A") * (1 if ord(c)-ord("Z")+13 > 0 else 0))
        elif "a" <= c <= "z":
            new_s += chr((ord(c)+13)%(ord("z")+1) + ord("a") * (1 if ord(c)-ord("z")+13 > 0 else 0))
        else :
            new_s += c
    print(new_s)