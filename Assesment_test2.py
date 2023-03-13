#Ques: Use for, .split(), and if to create a Statement that will print out words that start with 's':

#Ans:-
# st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     if word[0]=='s':
#         print(word)

#Ques: Use range() to print all the even numbers from 0 to 10.

#Ans:-

# for i in range(2,11,2):
#  print(i)

#Ques:- Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

#Ans:-

# for i in range(1,51):
#  if i % 3 == 0:
#      print(i)

#Ques:- Go through the string below and if the length of a word is even print "even!"

#Ans:-


# st = 'Print every word in this sentence that has an even number of letters'
# l=len(st)
# if l%2==0:
#     print("Even")
# else:print("Odd")

#Ques:- Write a program that prints the integers from 1 to 100.
#  But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

#Ans:- 

# for i in range(1,101):
#     if i%5==0 and i%3==0: print("FizzBuzz")
#     elif i%3==0: print("Fizz")
#     elif i%5==0: print("Buzz")
#     else: print(i)

#Ques-Use a List Comprehension to create a list of the first letters of every word in the string below:

#Ans:-
# st = 'Create a list of the first letters of every word in this string'
# s=[]
# for word in st.split():
#     s.append(word[0])

# print(s)
