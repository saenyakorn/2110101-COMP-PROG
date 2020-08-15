dic = {}

def text2keys(text):
    new_text = ""
    for c in text.lower():
        new_text += (str(dic[c]) if ('a' <= c <= 'z' or c == " ") else "") + " "
    return new_text
def keys2text(keys):
    new_text = ""
    for c in keys.split():
        new_text += str(dic[c])
    return new_text

if __name__ == "__main__":
    e = 0
    for i in range(ord('z')-ord('a')+1):
        x = i-e
        ch = chr(i+ord('a'))
        nm = str(x//3+2)*(x%3+1)
        if ch == 's' or ch== 'z':
            e += 1
            nm = str(x//3+1)*4
        dic.update({ch:nm})
        dic.update({nm:ch})
    dic.update({'0':" "})
    dic.update({" ":'0'})
    exec(input().strip())

