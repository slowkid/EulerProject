"""
Summation of primes
Problem 10
Published on 08 February 2002 at 06:00 pm [Server Time]
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
print __doc__


from problem3 import get_prime_gen


def primes_sieve(limit):
    """
    Too slow.  Takes too long even at lower limits like 100000.
    """
    limitn = limit + 1
    primes = range(2, limitn)

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

def primes_sieve2(limit):
    """
    This solution overflows about a certain limit size.  Won't work in this case.
    """
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, limit, i):  # Mark factors non-prime
                a[n] = False
                
def sundaram3(max_n):
    """
    This algorithm is insanely fast.  Only taking around a second to execute even for 
    a limit of 2000000.
    """
    numbers = range(3, max_n + 1, 2)
    half = (max_n) // 2
    initial = 4

    for step in xrange(3, max_n + 1, 2):
        for i in xrange(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)

        if initial > half:
            return [2] + filter(None, numbers)
        
def solve():
    """
    This algorithm is absurdly slow because the prime gen is so slow.
    """
    pgen = get_prime_gen()    
    result = 0
    for p in pgen:
        if p < 2000000:
            print p
            result += p
        else:
            break
    return result

def solve():
    return sum(sundaram3(2000000))


if __name__ == "__main__":
    print "SOLUTION=", solve()    
