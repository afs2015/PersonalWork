# FibonacciGenerator
# Purpose: Fibonacci Sequence Generator

def genFib():
    '''Generator which calculates Fibonacci numbers.
	Yields next Fibonacci number in sequence'''

    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)

    while True:
    # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next


def getFib(fib):
    '''Wrapper function that returns the next Fibonacci number.
	Returns an (int)'''
    return next(fib)

def main():
    # Create instance of Fibonacci generator
    fib = genFib()

    choice = int(input("Pick a selection of Fibonacci numbers to be generated: "))

    while choice >= 0:
        print getFib(fib)
        choice -= 1

if __name__=='__main__':
    main()