num=int(input())
arr=[]
arr = list(map(int, input().split()))
num2=int(input())
arr2=[]
arr2 = list(map(int, input().split()))

arr=set(arr)
arr2=set(arr2)

print(len(arr.intersection(arr2)))
    