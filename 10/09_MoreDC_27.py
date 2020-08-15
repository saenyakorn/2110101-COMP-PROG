def knows(R,x,y):
    return bool(y in R[x])

def is_celeb(R,x):
    if len(R[x]) > 0 and not(len(R[x])==1 and x in R[x]):
        return False
    for k,v in R.items():
        if k!=x and not knows(R,k,x): 
            return False
    return True

def find_celeb(R):
    for k,v in R.items():
        if is_celeb(R,k):
            return k
    return None

def read_relations():
    R = {}
    while True:
        d = input().split()
        if len(d) == 1:
            break
        if d[0] in R:
            R[d[0]].add(d[1])
            if d[1] not in R: R[d[1]] = set()
        else:
            if d[0] == d[1]: R[d[0]] = set()
            else: R[d[0]] = {d[1]}
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)

exec(input().strip())
# main()
# Ploy Pat
# Ploy Boy
# Eak Pat
# Boy Pat
# Poom Pat
# Boy Eak
# q

# main() 
# Ploy Pat 
# Ploy Boy 
# Eak Pat 
# Boy Pat 
# Poom Pat 
# Boy Eak 
# Noo-sa Tim 
# q