# def placeValue(N, num):
     
#     total = 1
#     value = 0
#     rem = 0
     
#     while (True):
#         rem = N % 10
#         N = N // 10
 
#         if (rem == num):
#             value = total * rem
#             break
#         total = total * 10
         
#     return value



import re


def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman = ""
    while number:
        div = int(number/num[i])
        if div != 0:
            number %= num[i]
  
        while div:
            roman += sym[i]
            div -= 1
        i -= 1
    
    return roman



number = 999
print(printRoman(number))
number = 3
number = 58