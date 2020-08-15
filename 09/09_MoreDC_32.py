def first_fit(L,e): 
    for i in range(len(L)):
        if sum(L[i])+e <= 100:
            L[i].append(e)
            return
    L.append([e])
    return
def best_fit(L,e): 
    max_i,max_sum = -1,-1
    for i in range(len(L)):
        if sum(L[i])+e <= 100 and max_sum < sum(L[i]):
            max_sum,max_i = sum(L[i]),i
    if max_i >= 0: L[max_i].append(e)
    else : L.append([e])
    
def partition_FF(D):
    L = []
    for i in range(len(D)):
        first_fit(L,D[i])
    return L

def partition_BF(D):
    L = []
    for i in range(len(D)):
        best_fit(L,D[i])
    return L

if __name__ == "__main__":
    exec(input().strip())
