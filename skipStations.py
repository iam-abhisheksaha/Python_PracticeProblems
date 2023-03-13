

testCases=input("Enter the number of testCases:- ")
# print(testCases)
i=0
while i<=len(testCases):
    
    btwStation=int(input("Enter the number of stations between A and B: "))
    totalStaions=2+btwStation
    # print(totalStaions)
    count=1
    if totalStaions%2==1:
        count=count+1
    if totalStaions%3==1:
        count=count+1
    
    print(count)
    i=i+1