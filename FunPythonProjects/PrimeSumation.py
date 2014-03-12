from math import sqrt
def sum_primes(minlimit,limit):
    sieve = range(limit+1); sieve[1] = 0
    for n in xrange(minlimit, int(sqrt(limit))+1):
        if sieve[n] > 0:
            for i in xrange(n*n, limit+1, n): sieve[i] = 0
    return sum(sieve)