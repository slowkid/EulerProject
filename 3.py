"""
Largest prime factor
Problem 3
Published on 02 November 2001 at 06:00 pm [Server Time]

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from itertools import ifilter, count
import cProfile as profile

#----------------------------------------------------------------------------------
#Here is an ingenious solution found on the web that creates an iterable that
#returns a sequence of primes.

def get_prime_gen():
    """
    This works for a couple of reasons:

    A) Because of python's short-cicuit evaluation of booleans.
        In the case of "and", if first parameter is false, false is returned
        and 2nd parameter is not evaluated. i.e. no append happens in this
        context.
    B) Because of a quirk of lists as mutable objects when used as default
        parameters to a function ( even a lambda function ) whereby the list
        retains state between calls to the function.  i.e. list of known primes
        grows with successive iterations.

    See Python itertools documentation for ifilter and count.

    An obvious optimization to this would skip all even numbers after 2 and
        cut the number of iterations in half.
    """    
    return ifilter(
        lambda n, primes=[]:
            all(n%p for p in primes) and not primes.append(n), 
            count(2)
        )

"""
#Usage example.  Prints the first 10 prime numbers:
primes = get_prime_gen()
print "First 10 primes ="
for _ in range(10): print primes.next()
print "\n"
"""

#----------------------------------------------------------------------------------

def my_count():
    yield 2
    c = count(3,2)
    while True:
        yield next(c)

def get_prime_gen2():
    """
    A small optimization to the above algorithm prime_gen.  The my_count function only
    returns [2,3,all odd numbers...]
    """        
    return ifilter(
        lambda n, primes=[]:
            all(n%p for p in primes) and not primes.append(n), 
            my_count()
        )

"""
#Usage example.  Prints the first 10 prime numbers:
primes = get_prime_gen2()
print "First 10 primes ="
for _ in range(10): print primes.next()
print "\n"
"""

#----------------------------------------------------------------------------------
        
def print_prime_factors(number, primes):
    print "\n#----------------------------------------------------------------------------\n"
    print "THE PRIME FACTORS OF %s ARE: " % ("{:,}".format(number),)    
    while True:
        n = next(primes)
        if n > number:
            break
        if not number % n:
            number = number / n
            print n
    print "\n#----------------------------------------------------------------------------\n"
target = 600851475143
profile.run("print_prime_factors(target, get_prime_gen2())")
