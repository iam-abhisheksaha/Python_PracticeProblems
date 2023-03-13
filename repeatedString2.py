
import math
import os
import random
import re
import sys


def repeatedString(s, n):
    # Write your code here
    if len(s) == 1 and s[0] == 'a':
        print(n)
    else:
        s_list=list(s)
        a_counter=0
        divide_counter=0
        count=0
        for i in range(len(s_list)):
            if s_list[i]=='a':
                a_counter+=1
                
        while n>0:
            # remainder=n%len(s_list)
            n=n/len(s_list)
            count+=1
        
        # print(int(remainder))
        print(count)
        # print(len(s_list))

if __name__ == '__main__':


    s = input()

    n = int(input().strip())

    repeatedString(s, n)

