# End

from hashlib import new


n = "100111000010"
length = len(n)
if(length % 4 != 0):
    countZero = length % 4
    i = 0
    while i < countZero:
        n = n + "0"
        length = len(n)
        if(length % 4 == 0):
            break
        i += 1
    print(n)

if(length % 4 == 0):
    i = 0
    k = 4
    j = 0
    sum = "0000"
    while k <= length:
        part = n[j:k]
        # print(part)
        sum = bin(int(sum, 2) + int(part, 2))
        sum = sum[2:]
        temp_sum = sum
        j = k
        k = k+4

    carry_lenght = len(sum)-4
    temp = sum[carry_lenght-1]
    sum = sum[carry_lenght:]
    sum = int(sum, 2) + int(temp, 2)
    sum = bin(sum)
    sum = sum[2:]

sum_list = []

for i in sum:
    sum_list.append(i)

i = 0
while i < len(sum):

    if sum_list[i] == '1':
        sum_list[i] = '0'
    else:
        sum_list[i] = '1'
    i += 1
sum = ''.join(sum_list)

print(sum)
print(temp_sum)

# Receiving End


new_sum = int(temp_sum, 2)+int(sum, 2)
new_sum = bin(new_sum)
new_sum = new_sum[2:]
# print(new_sum)
carry_lenght = len(new_sum)-4
temp = new_sum[carry_lenght-1]
new_sum = new_sum[carry_lenght:]
new_sum = int(new_sum, 2) + int(temp, 2)
new_sum = bin(new_sum)
new_sum = new_sum[2:]

print(new_sum)
count = 0
for i in new_sum:

    if i == '0':
        print("Discarded")
        break
    else:
        count += 1

if(count == 4):
    print("Data is Secure")
