import itertools


def threeSumClosest(nums,target):
        data = list(itertools.combinations(nums,3))
        data = (list(set(data)))
        temp = []
        smallest = 0
        diffrence = target
        for i in data:
            add = sum(i)
            # print(add)
            if (add < target and abs(add) != target) or (add > target and abs(add) != target):
                # print(add)
                if (diffrence >= abs(target - (add))):
                    diffrence = abs(target - abs(add))
                    smallest = add
                    # print(smallest)

        if(len(data)==1):
            return sum(data[0])
        else:
            print(smallest)
            
        


nums = [-1,2,1,-4]
target = 1
threeSumClosest(nums, target)
nums = [1,1,1,0]
target = -100
threeSumClosest(nums, target)