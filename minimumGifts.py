from ast import JoinedStr
from unittest import TestCase


TestCases=input("Enter number of tests to run:- ")

j=0
while j<=len(TestCases):
    temp=int(input("Enter the Size:- "))
    employee=[]
    for i in range(temp):
        # print(i)
        rank=int(input("Enter the Rank:- "))
        employee.append(rank)
    gifts=1
    # print(employee)
    i=1
    while i<len(employee):
        # print(employee[i])
        if(employee[i]>employee[i-1]):
            gifts+=2
        elif(employee[i]<employee[i-1]):
            gifts+=1
        i=i+1
    
    print(gifts)
    j=j+1
        