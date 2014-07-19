"""
Smallest multiple
Problem 5
Published on 30 November 2001 at 06:00 pm [Server Time]
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def get_divisors(number):
    result = []
    for d in range(number,1,-1):
        if not number % d:
            result.append(d)
    return result

for i in range(20,10,-1):
    print get_divisors(i)
    
def solution():
    result = 1
    for n in range(20,10,-1):
        result *= n
    print result/16/15/12
    
solution()