import itertools

def fourSums(nums, target):
    data = list(itertools.combinations(nums, 4))
    # print(data)
    mader = []
    for i in data:
        temp = sum(i)
        if temp == target:
            mader.append(i)
    
    return (list(set(mader)))





nums = [2,2,2,2,2]
target = 8
fourSums(nums, target)