# Write a function that computes the volume of a sphere given its radius.

#Ans:-
# def vol_sphere(radius):
#     vol=4/3*3.14*radius**3
#     return vol

# print(vol_sphere(2))

# Write a function that checks whether a number is in a given range (inclusive of high and low)

#Ans:-
# def check_range(num,min,max):
#     for i in range(min,max):
#         if i==num: return True
#         else: pass
#     return False

# print(check_range(3,1,10))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# def upper_lower(string):
#     upper_case=0
#     lower_case=0
#     for i in range(0,len(string)):
#         if string[i].isupper(): upper_case += 1
#         elif string[i].islower(): lower_case += 1

#     return (upper_case,lower_case)

# upper,lower= upper_lower('Hello Mr. Rogers, how are you this fine Tuesday?')


# print(f'No. of Upper case characters: {upper}')
# print(f'No. of Lower case Characters : {lower}')


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# def unique_list(string):
#     return set(string)

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Write a Python function to multiply all the numbers in a list.

# def multiply_list(string):
#     multi=1
#     for i in range(0,len(string)):
#         multi=multi*string[i]

#     return multi

# print(multiply_list([1, 2, 3, -4]))

# Write a Python function that checks whether a word or phrase is palindrome or not.

# def palindrome_check(string):

#     string=string.replace(" ", "")
#     return string==string[::-1]


# print(palindrome_check('helleh'))

def mutate_string(string, position, character):
    string.pop(position)
    string.insert(position,character)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)









