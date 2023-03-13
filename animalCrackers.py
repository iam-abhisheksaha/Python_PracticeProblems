# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def same_letter(string):
    temp=[]
    temp.append(string[0])
    i=0
    while i!=len(string):
        if string[i]==' ':
            temp.append(string[i+1])
            break
        i=i+1
    if temp[0]==temp[1]:
        return True
    else:
        return False
    
print(same_letter('Crazy Kangaroo'))