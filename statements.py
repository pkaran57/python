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
print('any(L) = {}, all(L) = {}'.format(any(L), all(L)))  # Aggregate truth

X = (1 +
     2)  # using newline is okay here since brackets are used

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
else:
    print("This will execute")  # Run if didn't exit loop with break

print("'list' from the for statement above carries over! X = ", X)

L = [(1, 2, 3), (4, 5, 6)]
for (a, *b, c) in L: print('a = {}, b = {}, c = {}'.format(a, b, c))        # complex variable assignments an be used in a for loop

X, Y = 0, 99

while X < Y:
    print('Setting X to a value higher than 99!')
    X = 100

while False:
    print("This won't execute")
else:  # Optional else
    print('Optional else from while statement')  # Run if didn't exit while loop with break

if True:
    pass  # empty placeholder

if True:
    ...  # empty placeholder, same as pass

while True:
    if X == 100: break  # continue is also a keyword which can be used similarly
else:
    print("This won't execute")

# No switch statements in Python, use dictionaries instead:
branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}
print('dictionary switch - ', branch.get('choice', 'default'))
