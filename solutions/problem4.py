"""
Largest palindrome product
Problem 4
Published on 16 November 2001 at 06:00 pm [Server Time]

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

print "problem4"

for a in range(1000):
    for b in range(1000):
        c = a * b

print "done"

def is_palindrome(candidate):
    """
    Determine if candidate is palindromic. candidate must be 'int' or 'str'
    """
    if type(candidate) in (int, long):
        candidate = str(candidate)
    if type(candidate) != str:
        raise TypeError("is_palindrome(): candidate is not 'str' or 'int' type. type(candidate) = %s" % type(candidate))
    candidate = 'c' + candidate
    
    print candidate[0], candidate[-1]
    
    
    
print is_palindrome(314159265358979323846264338327950288419716939937510582)