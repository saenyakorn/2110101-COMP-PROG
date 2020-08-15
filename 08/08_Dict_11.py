def reverse(dic):
    new_dic = {}
    for k,v in dic.items():
        new_dic[v] = k
    return new_dic

def keys(dic,val):
    ls = []
    for k,v in dic.items():
        if v == val:
            ls += [k]
    return ls

if __name__ == "__main__":
    exec(input().strip())