def total(dic):
    total = 0
    for k,v in dic.items():
        total += k*v
    return total
def take(dic,tk):
    for k,v in tk.items():
        if k in dic: dic[k] += v 
        else: dic.update({k:v})
def pay(dic,mon):
    py,i = {},0
    money = sorted([[-k,v] for k,v in dic.items()])
    money = [[-k,v] for k,v in money]
    while mon > 0:
        if i == len(money):
            return {}
        k,v = money[i]
        coin = v if mon//k > v else mon//k
        if v > 0 and coin > 0:
            py[k] = coin
            mon -= coin*k
        i += 1
    for k,v in py.items():
        dic[k] -= v
    return py

if __name__ == "__main__":
    exec(input().strip())