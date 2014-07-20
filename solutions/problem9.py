"""
Special Pythagorean triplet
Problem 9
Published on 25 January 2002 at 06:00 pm [Server Time]
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
print __doc__

import operator

def product(iterable):
    return reduce(operator.mul, iterable, 1)

def list_pythagorean_triples(limit):
    """
    This function works....but it sucks...for so many reasons.  I can't see how...
    but I feel like I could eliminate the inner loop
    """
    limit += 1
    for a in range(3,limit):
        for b in range(a,limit-a):
            for c in range(b,limit-a-b):
                if a ** 2 + b ** 2 == c ** 2:
                    yield (a, b, c)

def solve():
    #return [product(pgt) for pgt in list_pythagorean_triples(1001) if sum(pgt) == 1000]
    for pgt in list_pythagorean_triples(1000):
        if sum(pgt) == 1000:
            return product(pgt)

if __name__ == "__main__":
    print "SOLUTION=", solve()
