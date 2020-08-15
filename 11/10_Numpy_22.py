import numpy as np
def mult_table(nrows, ncols):
     return np.array([np.arange(1,nrows+1)]).T * np.array([np.arange(1,ncols+1)])

exec(input().strip())