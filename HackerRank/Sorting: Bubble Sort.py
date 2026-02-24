#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    length = len(a) -1
    count = 0
    for n in range(length,0,-1):
        for y in range(n):
            if a[y] > a[y+1]:
                a[y+1] , a[y] = a[y] , a[y+1]
                count += 1
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[length]}')
                
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
