

from re import sub
import math

number=input("Enter the Number:- ")

subSting=set()
prontic=[]
for i in range(0,len(number)):
    for j in range(i,len(number)):
        temp=int(number[i:j+1])
        subSting.add(temp)

subSting=sorted(subSting)
print(subSting)

# for num in subSting:
#     for val in range(1,int(math.sqrt(num))+1):
#         if (val*(val+1)==num):
#             prontic.append(num)
#             break

for i in subSting:
    for val in range(1,int(i)):
        if (val*(val+1)==i):
            prontic.append(i)
            break
        
print(prontic)
        
        