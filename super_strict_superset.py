A=list(map(int, input().rstrip().split()))
loop_count=int(input())
for i in range(loop_count):
    sub_set1=list(map(int, input().rstrip().split()))
    
    sub_set2=list(map(int, input().rstrip().split()))
    A=set(A)
    if sub_set1==A or sub_set2==A:
        print(False)
    elif A==A.union(sub_set1) and A==A.union(sub_set2):
        print(True)
    else:
        print(False)