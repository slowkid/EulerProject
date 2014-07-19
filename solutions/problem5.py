"""
Smallest multiple
Problem 5
Published on 30 November 2001 at 06:00 pm [Server Time]
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from fractions import gcd


def lcm(a, b):
    return a * b / gcd(a, b)

def solve():
    return reduce(lcm, range(1,20+1))


if __name__ == "__main__":    
    print solve()
