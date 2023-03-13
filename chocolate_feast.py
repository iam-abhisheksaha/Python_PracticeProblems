

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    total_bars= int(n/c)
    total_wrapper=int(n/c)
    while total_wrapper!=0:
        if total_wrapper>=m:
            total_bars=total_bars+1
            total_wrapper=total_wrapper-m
            total_wrapper=total_wrapper+1
        else:
            break
    
    return total_bars


if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)
        print(result)