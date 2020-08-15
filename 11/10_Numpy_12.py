import numpy as np

def toCelsius( f ):
    return ((f-32)/9)*5
def BMI( wh ):
    return wh[:,0]/(wh[:,1]/100)**2
def distanceTo( p, Points ):
    d = np.array(p) - Points
    return (d[:,0]**2+d[:,1]**2)**0.5

exec(input().strip())