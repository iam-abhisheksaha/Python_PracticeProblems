def pow_string(my_string):
    for i in my_string:
        
        try:
            print(i**2)
        except TypeError:
            print('There was a Type error')


pow_string(['a', 'b', 'c', 4])
