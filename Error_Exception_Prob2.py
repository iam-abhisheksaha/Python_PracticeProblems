def divide(x,y):
    try:
        result =x/y
        print(result)
    except ZeroDivisionError:
        print("One of the assign number is 0")
    finally:
        print("All Done!")

x=int(input("Enter a Divisor value:- "))
y=int(input("Enter a Divident Value:- "))

divide(x,y)
