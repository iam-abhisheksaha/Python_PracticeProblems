# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(num):
    i=0
    code=[0,0,7,'x']
    for i in num:
        if i==code[0]:
            code.pop(0)

    return len(code)==1

print(spy_game([1,0,2,4,0,5,7]))
