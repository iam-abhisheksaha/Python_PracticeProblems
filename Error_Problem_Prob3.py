def ask():
    while True:
        try:
            num =int(input('Input an integer: '))
            square= num**2
            print(f'The Square of the number is {square}')
            break
        except:
            print('An error occurred! Please try again')
        finally:
            print('Please Try Again')

ask()
