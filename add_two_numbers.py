def addTwoNumbers(l1,l2):
    l1_num = int("".join(map(str,l1)))
    l2_num = int("".join(map(str,l2)))
    sum = l1_num + l2_num
    # print(sum)
    sum = str(sum)
    sum_list = []
    for i in sum:
        sum_list.append(int(i))
    
    return(sum_list[::-1])




l1 = [2,4,3]
l2 = [5,6,4]
addTwoNumbers(l1, l2)