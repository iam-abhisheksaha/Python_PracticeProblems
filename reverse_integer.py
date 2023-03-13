from hashlib import new
import re


def reverseInteger(x):
    if x < 0:
        sign = "-"
        x = abs(x)
        x = str(x)
        new_number = sign + x[::-1]
    else:
        x = str(x)
        new_number = x[::-1]
    
    return int(new_number)



x = 210
print(reverseInteger(x))