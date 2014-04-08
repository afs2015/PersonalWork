# FibonacciGenerator
# Purpose: Fibonacci Sequence Generator

def genFib():
    '''Generator which calculates Fibonacci numbers.
    Yields next Fibonacci number in sequence. Starts at 0'''
    
    fibn_1, fibn_2 = 0, 1 #fib(n-1), fib(n-2)

    while True:
    # fib(n) = fib(n-1) + fib(n-2)
        yield fibn_1
        fibn_1, fibn_2 = fibn_2, fibn_1 + fibn_2

def getFib(fib):
    '''Wrapper function that returns the next Fibonacci number.
	Returns an (int)'''
    return next(fib)

def getFibRec(n):
    ''' Function which calculates Fibonacci numbers recursively. Starts at 0'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getFibRec(n-2) + getFibRec(n-1)

def main():
    # Create instance of Fibonacci generator
    fib = genFib()

    choice = int(input("Pick a selection of Fibonacci numbers to be generated: "))

    while choice >= 0:
        print getFib(fib)
        choice -= 1

if __name__=='__main__':
    main()