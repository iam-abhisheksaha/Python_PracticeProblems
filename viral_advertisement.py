
import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    i=1
    liked=int(5/2)
    cumulative=liked
    while i<n:
        shared=liked*3
        liked=int(shared/2)
        cumulative=cumulative+liked
        i=i+1
        
    return cumulative
    


if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)
    print(result)