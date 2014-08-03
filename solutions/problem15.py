#!/usr/bin/env python
"""
Lattice paths
Problem 15
Published on 19 April 2002 at 06:00 pm [Server Time]

Starting in the top left corner of a 2x2 grid, and only being able to move to the 
    right and down, there are exactly 6 routes to the bottom right corner.

**** see p_015.gif for this example solution of the 2x2 grid ****

How many such routes are there through a 20x20 grid?
"""
#------------------------------------------------------------------------------ 
from math import factorial as fact

#------------------------------------------------------------------------------ 
def calc_binomial_coefficent(n, k):
    """
    Binomial coefficient is a way of calculating a combination.  It's read as
    n choose k.  Example:  I have 4 things and want to find all pair combinations.
    So its 4 choose 2.  The answer to this is 6,
     
    _nC_k and (n; k)
    _nC_k = (n; k) = (n!)/((n-k)!k!)  
     
    http://mathworld.wolfram.com/BinomialCoefficient.html has a decent reference
    for calculating these.
    """
    
    return (fact(n)/(fact(n-k) * fact(k)))

#------------------------------------------------------------------------------
def solve():
    """
    The number of lattice paths from the origin (0,0) to a point (a,b) is the 
    binomial coefficient (a+b; a) (Hilton and Pedersen 1991).
    
    http://mathworld.wolfram.com/LatticePath.html is a quick reference
    """
    return calc_binomial_coefficent(20+20,20)
 
#------------------------------------------------------------------------------ 
def main():
    print "PROBLEM:\n"
    for line in __doc__.strip().split('\n'):
        print '\t', line    
    print "\nSOLUTION:"
    print "\n\t", solve()

#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    main()