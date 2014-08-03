#!/usr/bin/env python
"""
Power digit sum
Problem 16
Published on 03 May 2002 at 06:00 pm [Server Time]

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
#------------------------------------------------------------------------------ 
def solve():
    return sum([int(n) for n in str(2**1000)])

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