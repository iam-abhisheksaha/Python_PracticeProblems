n = "100111000010"

length = len(n)
n1 = "1001"
n2 = "1100"
n3 = "0010"

sum = int(n1)+int(n2)+int(n3)
sum = bin(sum)
sum = sum[2:]
temp = sum[0]
sum = sum[1:]
sum = int(sum, 2) + int(temp, 2)
sum = bin(sum)
sum = sum[2:]

print(sum)

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


new_sum = int(n1, 2)+int(n2, 2)+int(n3, 2)+int(sum, 2)
new_sum = bin(new_sum)
new_sum = new_sum[2:]
temp2 = new_sum[0]
new_sum = new_sum[1:]

new_sum = int(new_sum, 2) + int(temp2, 2)
new_sum = bin(new_sum)
new_sum = new_sum[2:]
print(new_sum)
