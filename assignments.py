# Assignment Statement Forms
tuple = spam, ham = 'yum', 'YUM'  # Tuple assignment (positional)
list = [spam, ham] = ['yum', 'YUM']  # List assignment (positional)
a, b, c, d = 'spam'  # Sequence assignment,  wherever the starred name shows up, it will be assigned a list that collects every unassigned name at that position
a, *b, c = 'spam'  # Extended sequence unpacking (Python 3.X)
spam = ham = 'lunch'  # Multiple-target assignment

print('\nAssignment form general demo - \n')
print(
    'a = {}, b = {}, c = {}, d = {}\n spam = {}, ham = {}\n tuple = {}\n list = {}'.format(a, b, c, d, spam, ham, tuple,
                                                                                           list))

# Python assigns items in the sequence on the right to variables in the sequence on the left by position, from left to right:

set = [a, b, c] = {1, 2, 3}  # a = 1 and so on
string = (a, b, c) = "ABC"  # a = A and so on
print('set = {}, string = {}'.format(set, string))
print('a = {}, b = {}, c = {}'.format(a, b, c))

for ((a, b), c) in [(('S', 'P'), 'AM')]: print('From for loop - a = {}, b = {}, c = {}'.format(a, b, c))

print('\nBOUNDARY CASES demo - \n')
seq = [1, 2, 3, 4]
a, b, c, *d = seq
print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d))
a, b, c, d, *e = seq
print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d))
*a, = seq
print('a = ', a)

# a, *b, c, *d = seq        SyntaxError: two starred expressions in assignment
# a, b = seq                ValueError: too many values to unpack (expected 2)
# *a = seq                  SyntaxError: starred assignment target must be in a list or tuple
