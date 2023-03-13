#Use the iter() function to convert the string below into an iterator:

s = 'hello'

s_iter = iter(s)
for s in s_iter:
    print(s)