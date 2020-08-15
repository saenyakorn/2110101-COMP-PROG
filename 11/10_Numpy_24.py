import numpy as np
import sys
def peak_indexes(x):
    return (np.arange(x.shape[0])[(np.append(np.array(x[1:]),[sys.maxsize]) < x) & (x > np.append([sys.maxsize],np.array(x[:-1])))])
def main():
    d = np.array([float(e) for e in input().split()]) 
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos])) 
    else:
        print("No peaks")

exec(input().strip())