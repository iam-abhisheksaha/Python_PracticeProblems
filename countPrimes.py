# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    #check for 0 or 1 input
    if num<2:
        return 0
    
    # number is 2 or greater
    

    # Store our prime numbers
    primes=[2]

    # Counter upto the input num
    x=3

    # x is going through every number up to input num
    while x<=num:
        # Check if x is prime
        for i in range(3,x,2):
            if x%i==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
        
    print(primes)
    return len(primes)


print(count_primes(100))
