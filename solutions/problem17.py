#!/usr/bin/env python
"""
Number letter counts
Problem 17
Published on 17 May 2002 at 06:00 pm [Server Time]

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?


NOTE:
Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The 
use of "and" when writing out numbers is in compliance with British usage.
"""
#------------------------------------------------------------------------------ 
def split_triples(number):
    number = str(number)
    while number:
        yield int(number[-3:])
        number = number[:-3]

def convert_digit(digit):
    digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    if digit < 0 or digit > 9:
        raise ValueError("Out of range: digit = %s" % digit) 
    
    return digit_words[digit] 

def convert_double_digits(ddn):
    teen_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", 
                  "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_words = ["N/A", "N/A", "twenty", "thirty", "forty",
                  "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if ddn < 10:        
        result = convert_digit(ddn)        
    elif ddn > 9 and ddn < 20:
        result = teen_words[ddn-10]
    elif ddn > 19 and ddn < 100:
        tens, ones = divmod(ddn, 10)
        result = tens_words[tens]
        if ones > 0:
            result += "-%s" % convert_digit(ones)
    else:
        raise ValueError("Out of range: ddn = %s" % ddn)
    
    return result
    
def convert_triple_digits(tdn):
    if tdn < 1000:
        hundreds, ddn = divmod(tdn, 100)
        if hundreds:
            result = convert_digit(hundreds) + " hundred "
            if ddn:
                result += "and "
        else:
            result = ""        
        if ddn:
            result += "%s" % convert_double_digits(ddn)
    else:
        raise ValueError("Out of range: tdn = %s" % tdn)
    
    return result
    
def convert_number_to_words(number):
    """
    """
    triple_names = ["", "thousand", "million", "billion", "trillion"]
    triples = split_triples(number)
    
    result = ""
    for index, triple in enumerate(triples):
        #result = convert_triple_digits(triple)
        template = "%s %s"
        if index and triple:
            template += ", "
        if triple: 
            result = template % (convert_triple_digits(triple), triple_names[index]) + result
        if index > 0:
            #result += ", "
            pass
    return number, result

#------------------------------------------------------------------------------ 
def solve():
    pass

#------------------------------------------------------------------------------ 
def main():
    print "PROBLEM:\n"
    for line in __doc__.strip().split('\n'):
        print '\t', line    
    print "\nSOLUTION:"
    print "\n\t", solve()

#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    #main()
    print convert_number_to_words(123456789)
    #print convert_number_to_words(11101)
    print convert_number_to_words(1000000001)
    #print convert_number_to_words(1000001)
    #print convert_number_to_words(1001)
    print convert_number_to_words(101)
    print convert_number_to_words(1000)