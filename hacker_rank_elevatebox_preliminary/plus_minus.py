#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos=0
    neg=0
    ze=0
    n=len(arr)
    for i in arr:
        if(i>0):
            pos+=1
        elif(i<0):
            neg+=1
        else:
            ze+=1
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{ze/n:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
