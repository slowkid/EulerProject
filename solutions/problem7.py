#!/usr/bin/env python

"""
10001st prime
Problem 7
Published on 28 December 2001 at 06:00 pm [Server Time]


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

#------------------------------------------------------------------------------ 
from itertools import islice
from problem3 import get_prime_gen

#------------------------------------------------------------------------------ 
def nth(iterable, n, default=None):
    """
    Returns the nth item or a default value
    
    This is a nifty recipe found on the internet @ docs.python.org/2/library/itertools.html#recipes.  
    It's description seems misleading, though. It's not exactly returning the nth item.  It's returning 
    the item that would be at index n if the iterable were subscriptable.
    
    An example of this would be:
        nth(range(10),10) returns None since index 10 doesn't exist rather returning the 10th item which is 9  
    """
    return next(islice(iterable, n, None), default)

def solve():
    """
    Returns the solution to the problem statement in module.__doc__ shown above.
    """
    return nth(get_prime_gen(), 10000)

#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    print __doc__
    print "SOLUTION=", solve()
