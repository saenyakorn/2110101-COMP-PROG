import numpy as np
def read_data():
    w = [float(e) for e in input().split()] 
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    result = data[np.sum(data[:,1:]*weight,axis=1) < np.sum(data[:,1:]*weight)/data.shape[0]][:,:1]
    result = ', '.join([str(result[i][j]) for i in range(result.shape[0]) for j in range(result.shape[1])])
    print(result if result!="" else "None")

exec(input().strip())