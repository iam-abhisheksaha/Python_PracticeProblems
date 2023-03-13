

num=int(input())
name=[]
average_score=[]
i=0
while i<=num:
    temp, score1, score2, score3 = input(),int(input()),int(input()),int(input())
    average=score1+score2+score3/3
    name.append(temp)
    average_score.append(average) 
    i=i+1   

print(name,average_score)