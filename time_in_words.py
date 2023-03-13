

import math
import os
import random
import re
import sys
from num2words import num2words

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    if m==0:
        print(num2words(h) + " o'" + ' clock')
    if m<=30:
        if m==15:
            print('quater past ' + num2words(h))
        if m==30:
            print('half past ' + num2words(h))
        elif m!=30 and m!=15:
            print(num2words(m) + ' minutes past ' + num2words(h))
    elif m>30:
        if m==45:
            print('quarter to '+ num2words(h+1))
        elif m!=45:
            print(num2words(60-m) + ' minutes to '+ num2words(h+1))


if __name__ == '__main__':

    h = int(input().strip())

    m = int(input().strip())

    timeInWords(h, m)
