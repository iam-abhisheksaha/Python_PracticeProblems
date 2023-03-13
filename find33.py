# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find_33(list):
    i=0
    for i in range(0,len(list)-1):
        if list[i]==3 and list[i+1]==3:
            return True
        else: pass
        i=i+1
    
    return False

print(find_33([1,3,1,3]))