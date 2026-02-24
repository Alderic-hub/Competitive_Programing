#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    val = arr[n-1]
    m = n-1
    for n in range(m,0,-1):
        if arr[n-1] > val:
            arr[n] = arr[n-1]
        else:
            arr[n] = val
            break
        vals = list(map(str, arr))
        print(" ".join(vals))
    if val not in arr:
        arr[0] = val
    vals = list(map(str, arr))    
    print(" ".join(vals)) 
            
            
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
