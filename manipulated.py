from itertools import groupby
from platform import java_ver

temp_str=input('Enter a String:- ')
temp_str=list(temp_str)

stwr=[]
i=0
j=0
while i<len(temp_str):
    temp=[]
    temp.append(temp_str[i])
    temporary=temp_str[i]
    temp_str.remove(temp_str[i])
    i=i-1
    j=i+1
    while j<len(temp_str):
        if temporary==temp_str[j].upper() or temporary==temp_str[j].lower():
            temp.append(temp_str[j])
            temp_str.remove(temp_str[j])
        j=j+1
    i=i+1
    
    yoo=''.join(temp)
    stwr.append(yoo)
            

sorted_list = sorted(stwr, key=str.lower)

# print(sorted_list)
# print(len(sorted_list))
output_list=[]

middle=int(len(sorted_list)/2)
n=len(sorted_list)

if int(len(sorted_list)%2)!=0:
    # print('Even')
    n=n-1
    i=0
    while i<=int(middle-1) and n>=int(middle+1):
        output_list.append(sorted_list[i])
        output_list.append(sorted_list[n])
        i=i+1
        n=n-1
    output_list.append(sorted_list[middle])

else:
    n=n-1
    i=0
    # print(middle)
    while i<=int(middle-1) and n>=int(middle):
        output_list.append(sorted_list[i])
        output_list.append(sorted_list[n])
        i=i+1
        n=n-1
    
print(''.join(output_list))

    
    