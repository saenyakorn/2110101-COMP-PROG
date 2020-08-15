def no_lowercase(pw):
    new_pw = pw.upper()
    return new_pw == pw

def no_uppercase(pw):
    new_pw = pw.lower()
    return new_pw == pw

def no_number(pw):
    for c in pw:
        if "0" <= c <= "9": return 0
    return 1

def no_symbol(pw):
    sym= ""
    for c in pw:
        sym += "" if "A"<=c<="Z" or "a"<=c<="z" or "0"<=c<="9" else c
    return not len(sym)

def repeating(sub):
    return sub[0]==sub[1] and sub[1]==sub[2] and sub[2]==sub[3]

def number_seq(sub):
    kb = "1234567890123456789"
    rb = "9876543210987654321"
    return sub in kb or sub in rb

def letter_seq(sub):
    ck = True
    sub = sub.lower()
    for c in sub:
        if not "a"<=c<="z": return False
    for i in range(1,len(sub)):
        if not (ord(sub[i])-i == ord(sub[0]) or ord(sub[i])+i == ord(sub[0])):
            ck = False
    return ck

def keyboard(sub):
    sub = sub.lower()
    kb = ["!@#$%^&*()_+","qwertyuiop","asdfghjkl","zxcvbnm"]
    rb = ["+_)(*&^%$#@!","poiuytrewq","lkjhgfdsa","mnbvcxz"]
    for item in kb:
        if sub in item: return True;
    for item in rb:
        if sub in item: return True;
    return False

if __name__ == "__main__":
    pw = input().strip()
    e = []
    if len(pw) < 8:
        e += ["Less than 8 characters"]
    if no_lowercase(pw):
        e += ["No lowercase letters"]
    if no_uppercase(pw):
        e += ["No uppercase letters"]
    if no_number(pw):
        e += ["No numbers"]
    if no_symbol(pw):
        e += ["No symbols"]
    
    for i in range(len(pw)-3):
        sub = pw[i:i+4]
        if repeating(sub):
            e += ["Character repetition"]
            break
    for i in range(len(pw)-3):
        sub = pw[i:i+4]
        if number_seq(sub):
            e += ["Number sequence"]
            break
    for i in range(len(pw)-3):
        sub = pw[i:i+4]
        if letter_seq(sub):
            e += ["Letter sequence"]
            break
    for i in range(len(pw)-3):
        sub = pw[i:i+4]
        if keyboard(sub):
            e += ["Keyboard pattern"]
            break
    
    if len(e)==0:
        print("OK")
    else :
        for item in e:
            print(item)