'''
Indentation

Python doesn’t care how you indent (you may use either spaces or tabs), or how much you indent (you may use any number of spaces or tabs). In fact, the indentation of one nested block can be totally different from that of another.
The syntax rule is only that for a given single nested block, all of its statements must be indented the same distance to the right. If this is not the case, you will get a syntax error, and your code will not run until you repair its indentation to be consistent.
As a rule of thumb, you probably shouldn’t mix tabs and spaces in the same block in Python, unless you do so consistently; use tabs or spaces in a given block, but not both
'''

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

# No switch statements in Python, use dictionaries instead:
branch = {'spam': 1.25, 'ham':  1.99, 'eggs': 0.99}
print('dictionary switch - ', branch.get('choice', 'default'))

try:
    int('XYZ')
except:
    print('XYZ is not an int!')
else:
    print('This will run if no exception raised')

''' Truth Values and Boolean Tests

All objects have an inherent Boolean true or false value.
Any nonzero number or nonempty object is true.
Zero numbers, empty objects, and the special object None are considered false.
Comparisons and equality tests are applied recursively to data structures.
Comparisons and equality tests return True or False (custom versions of 1 and 0).
Boolean and and or operators return a true or false operand object.
Boolean operators stop evaluating (“short circuit”) as soon as a result is known.

if f1() or f2(): ...
Here, if f1 returns a true (or nonempty) value, Python will never run f2. To guarantee that both functions will be run, call them before the or:
tmp1, tmp2 = f1(), f2()
if tmp1 or tmp2: ...
'''

print('Empty string has following boolean value - ', 'true' if '' else 'false')
L = ['', 1, False, True, None]
L1 = [x for x in L if x]
print('All truth values in L1 = ', L1)
print('any(L) = {}, all(L) = {}'.format(any(L), all(L)))      # Aggregate truth