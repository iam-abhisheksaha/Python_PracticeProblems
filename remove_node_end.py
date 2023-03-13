def removeNode(head, node):

    index = len(head)-node

    # print(index)
    head.pop(index)
    print(head)



head = [1,2,3,4,5]
n = 2
removeNode(head,n)