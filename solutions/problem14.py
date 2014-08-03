#!/usr/bin/env python
"""
Longest Collatz sequence
Problem 14
Published on 05 April 2002 at 06:00 pm [Server Time]

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 > 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
#------------------------------------------------------------------------------ 
def get_collatz_seq(number):
    """
    This is cute.  It's recursive.  It sucks.  It runs past maximum recursion
    depth if solving the problem.  I guess you could solve this by a stackless
    implementation.  
    """
    if number == 1:
        return [number]            
    elif number%2:    #number is odd
        return [number] + get_collatz_seq(3 * number + 1)
    else:
        return [number] + get_collatz_seq(number / 2)
        
def get_collatz_seq(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1 
       seq.append(x)    # Added line
    return seq
    
#------------------------------------------------------------------------------ 
def solve():
    longest_chain = 1, [1]
    for n in range(1,1000000):
        seq = get_collatz_seq(n)
        chain = n, seq
        if len(chain[1]) > len(longest_chain[1]):
            longest_chain = chain
    return longest_chain[0]

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