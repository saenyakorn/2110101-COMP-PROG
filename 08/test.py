def total(pocket):
    return sum([value * amount for value, amount in pocket.items()])

def take(pocket, money):
    for value, amount in money.items():
        if value in pocket:
            pocket[value] += amount
        else:
            pocket[value] = amount

def pay(pocket, amt):
    types = sorted([[-value, amount] for value, amount in pocket.items()])
    types = [[-nValue, amount] for nValue, amount in types]
    toRemove = {}
    while amt > 0:
        if len(types) == 0:
            return {}
        value, amount = types[0]
        types = types[1:]
        amount = min(amount, amt // value)
        if amount == 0:
            continue
        amt -= value * amount
        toRemove[value] = amount
    for value, amount in toRemove.items():
        pocket[value] -= amount
    return toRemove

exec(input().strip())

'''
p={100:2, 50:2, 5:2, 1:2};print(total(p))

p={100:5};take(p,{100:2, 1:3});print(p)

p={100:5};take(p,{100:0, 1:0});print(p)

p={10:5, 1:7};print(pay(p, 12));print(p)

p={10:5, 1:7};print(pay(p, 18));print(p)

p={10:5, 1:7};print(pay(p, 100));print(p)

p={10:5, 1:7};print(pay(p, 57));print(p)

'''
