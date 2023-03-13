# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
#                      but returns the greater if one or both numbers are odd


def return_less(a,b):
    if a%2==0 and b%2==0 and a<b:
        return a
    elif a%2==0 and b%2==0 and a>b:
        return b
    elif a>b:
        return a
    else:
        return b

print(return_less(9,20))