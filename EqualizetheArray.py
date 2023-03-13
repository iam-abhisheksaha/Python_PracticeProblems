

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    frequencies = collections.Counter(arr)
    repeatCount ={}

    for key,value in frequencies.items():

        if 1:
            repeatCount[key]=value

    all_values = repeatCount.values()
    max_value =max(all_values)
    deleteCount=len(arr)-max_value
    
    # print(max_value)
    print(deleteCount)


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    equalizeArray(arr)