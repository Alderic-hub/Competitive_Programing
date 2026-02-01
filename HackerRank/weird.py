import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    arr = [n for n in range(6,21)]
    if n%2 == 1 or n in arr:
        print("Weird")
    else:
        print( "Not Weird")
