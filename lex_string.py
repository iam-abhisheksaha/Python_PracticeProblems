
from hashlib import new


def lexString(alphabets, findString):
    newString = ""
    for i in alphabets:
        if(i in findString):
            newString += i;
    
    if(len(newString) == len(findString)):
        print(newString)
    else:
        print("List Not Found")




test = int(input())
for i in range(test):
    alphabets = input()
    findString = input()
    lexString(alphabets, findString)