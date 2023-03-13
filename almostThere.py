# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    if abs(100 - n)<=10 or abs(200 - n)<=10:
        return True
    else: return False

print(almost_there(209))