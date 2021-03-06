"""
Even Fibonacci numbers
Problem 2
Published on 19 October 2001 at 06:00 pm [Server Time]

Each new term in the Fibonacci sequence is generated by
adding the previous two terms.

By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

print __doc__
#------------------------------------------
#it could happen this way
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

total = 0
f = fib()
n = f.next()
while n <= 4000000:    
    print n
    if n%2 == 0:            
        total += n
    n = f.next()

print "total=", total


#or it coould happen  this way
#------------------------------------------

def even_fib(limit):
    a, b = 0, 1
    while a < limit:
        if not a % 2:         
            yield a
        a, b = b, a + b

print sum(even_fib(4000000))

#Just a curiosity: boolean values as indicies
a=2
print ("a is odd", "a is even")[a % 2 == 0]
print ("a is even", "a is odd")[a % 2]
