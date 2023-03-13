# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or 
#                     if one of the integers is 20. If not, return False


def equal_twenty(a,b):
    if a+b==20 or a==20 or b==20: return True
    else: return False

print(equal_twenty(2,3))