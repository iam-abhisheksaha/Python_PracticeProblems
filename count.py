
from this import d


dict = {}
num_list = [1,2,1,2,2,3,4,5]

for i in num_list:
    if(dict.get(i) == None):
        dict[i] = 1
    else:
        dict[i] += 1

print(dict)
find_max = max(dict,key = dict.get)
print(find_max)