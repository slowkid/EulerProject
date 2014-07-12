""" Problem 2 docstring """
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
