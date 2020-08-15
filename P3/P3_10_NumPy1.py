import numpy as np
import sys

def eq(A, B, p):
    cnt,All = 0,1
    for i in range(len(A.shape)):
        All *= A.shape[i]
    cnt = A==B
    for i in range(len(A.shape)):
        cnt = sum(cnt)
    return cnt >= p/100*All

def closest_point_indexes(points, p):
    result = np.sum(points**2-p**2,axis=1)**0.5
    mn = np.min(result)
    ls = np.arange(points.shape[0])[result==mn]
    return ls

cnt = 0

def mergeSort(arr): 
    temp_arr = np.zeros(arr.shape)
    return _mergeSort(arr, temp_arr, 0, arr.shape[0]-1) 
  
def _mergeSort(arr, temp_arr, left, right): 
    inv_count = 0
    if left < right: 
        mid = (left + right)//2
        inv_count = _mergeSort(arr, temp_arr, left, mid) 
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right) 
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count 

def merge(arr, temp_arr, left, mid, right): 
    i = left     
    j = mid + 1 
    k = left     
    inv_count = 0

    while i <= mid and j <= right: 
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
  
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1

    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1

    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count

def number_of_inversions(A):
    return mergeSort(A)

exec(input().strip())

# print(closest_point_indexes(np.array([[9,9],[1,2],[10,10]]),np.array([1,1])))