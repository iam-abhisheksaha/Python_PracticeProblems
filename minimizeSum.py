

Size,maxChanges=input().split()
arr=[]
Size = int(Size)
i=0
for i in range(Size):
    temp=int(input())
    arr.append(temp)
    
# print(arr)
maxChanges=int(maxChanges)
for i in range(maxChanges):
    # print(i)
    maxValue=max(arr)
    maxIndex=arr.index(maxValue)
    maxValue=int(maxValue/2)
    arr[maxIndex] = maxValue

print(sum(arr))