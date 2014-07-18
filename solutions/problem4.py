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
    
    Notice the slicing notation in the return line.  Slice notation is
    [start:end:stride].  Any of these can be left blank and will default
    as follows: start == blank is beginning of str.  end == blank is end of
    string.  stride == blank is +1
    """
    if type(candidate) in (int, long):
        candidate = str(candidate)
    if type(candidate) != str:
        raise TypeError("is_palindrome(): candidate is not 'str' or 'int' type. type(candidate) = %s" % type(candidate))
        
    #return whether candidate == reverse of itself.  ie is a palindrome
    return candidate == candidate[::-1]
    
def main():
    largest = 0
    for a in range(100,1000):
        for b in range(100,1000):
            product = a * b
            if is_palindrome(product):
                if product > largest:
                    largest = product
    print(largest)

if __name__ == "__main__":
    #main()
    word = "thunderbox"
    print word[:]
    print word[::]
    print word[::1]
    print word[::-1]
    print word[::-2]
    print word[::-1][::-1]