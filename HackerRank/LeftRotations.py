
import math
import os
import random
import re
import sys

def rotateLeft(d, arr):
    ans = []
    limit =len(arr)
    for n in range(limit):
        if d >= limit:
            d = 0
        ans.append(arr[d])
        d+=1
    return ans
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
