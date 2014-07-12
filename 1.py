print sum([x for x in range(1000) if not(x%3) or not(x%5)])

for i in range(16):
    print i, i%3, i%5
    print (not(i%3) or not(i%5))
    print not(i%3 and i%5)

print sum([x for x in range(1000) if not(x%3 and x%5)])

#Shit my pants!

"""
class Number():
    def __init__(self, value):
        self.value = value        
    def is_a_multiple_of(self, number_set):
        for number in number_set:
            result = not(self.value%number)
            if result:
                return result

divisors = [3,5]
total = 0
for x in range(10):
    if 
"""
