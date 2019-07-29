# Assignment Statement Forms
tuple = spam, ham = 'yum', 'YUM'        # Tuple assignment (positional)
list = [spam, ham] = ['yum', 'YUM']    # List assignment (positional)
a, b, c, d = 'spam'             # Sequence assignment,  wherever the starred name shows up, it will be assigned a list that collects every unassigned name at that position
a, *b, c = 'spam'               # Extended sequence unpacking (Python 3.X)
spam = ham = 'lunch'            # Multiple-target assignment

print('\nAssignment form general demo - \n')
print('a = {}, b = {}, c = {}, d = {}\n spam = {}, ham = {}\n tuple = {}\n list = {}'.format(a, b, c, d, spam, ham, tuple, list))

# Python assigns items in the sequence on the right to variables in the sequence on the left by position, from left to right:

set = [a, b, c] = {1, 2, 3}    # a = 1 and so on
string = (a, b, c) = "ABC"        # a = A and so on
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
'''
Indentation

Python doesn’t care how you indent (you may use either spaces or tabs), or how much you indent (you may use any number of spaces or tabs). In fact, the indentation of one nested block can be totally different from that of another.
The syntax rule is only that for a given single nested block, all of its statements must be indented the same distance to the right. If this is not the case, you will get a syntax error, and your code will not run until you repair its indentation to be consistent.
As a rule of thumb, you probably shouldn’t mix tabs and spaces in the same block in Python, unless you do so consistently; use tabs or spaces in a given block, but not both
'''

print('\nStatements demo - \n')

X = (1 +
     2)     # using newline is okay here since brackets are used

X = 1

if X > 0: print('body of a compound statement can instead appear on the same line as the header in Python')

if X:
    print('X is True!')
elif not X:
    print('X is false')
else:
    print('X is neither 0 nor 1')

for X in ['This', 'is', 'a', 'list']:
    print(X)

print("'list' from the for statement above carries over! X = ", X)

X, Y = 0, 99

while X < Y:
    print('Setting X to a value higher than 99!')
    X = 100

if True:
    pass  # empty placeholder

while True:
    if X == 100: break    # continue is also a keyword which can be used similarly

try:
    int('XYZ')
except:
    print('XYZ is not an int!')
else:
    print('This will run if no exception raised')

