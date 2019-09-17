""" Truth Values and Boolean Tests

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
"""

X = (1 +
     2)  # using newline is okay here since brackets are used


def truthiness():
    print('Empty string has following boolean value - ', 'true' if '' else 'false')

    L = ['', 1, False, True, None]
    L1 = [x for x in L if x]
    print('All truth values in L1 = ', L1)
    print('any(L) = {}, all(L) = {}'.format(any(L), all(L)))  # Aggregate truth


def control_statements():
    X = 1

    # if statement
    if X > 0:
        print('body of a compound statement can instead appear on the same line as the header in Python')

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

    # for loop
    L = [(1, 2, 3), (4, 5, 6)]
    for (a, *b, c) in L: print('a = {}, b = {}, c = {}'.format(a, b, c))        # complex variable assignments an be used in a for loop

    X, Y = 0, 99

    # while statement
    while X < Y:
        print('Setting X to a value higher than 99!')
        X = 100

    # break and else
    while False:
        print("This won't execute")
    else:  # Optional else
        print('Optional else from while statement')  # Run if didn't exit while loop with break

    while True:
        if X == 100: break  # continue is also a keyword which can be used similarly
    else:
        print("This won't execute")

    # pass
    if True:
        pass  # empty placeholder

    if True:
        ...  # empty placeholder, same as pass

    # No switch statements in Python, use dictionaries instead:
    branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}
    print('dictionary switch - ', branch.get('choice', 'default'))


def iteration_protocol():
    """
    Iteration protocol

    * The iterable object you request iteration for, whose __iter__ is run by iter
    * The iterator object returned by the iterable that actually produces values during the iteration, whose __next__ is run by next and raises StopIteration when finished producing results

    A file object is its own iterator. Because files support just one iteration (they can’t seek backward to support multiple active scans), files have their own __next__ method and do not need to return a different object, they just return the same file object. Example: `iter(f) is f` returns true

    Lists and many other built-in objects, though, are not their own iterators because they do support multiple open iterations—for example, there may be multiple iterations in nested loops all at different positions. For such objects, we must call iter to start iterating
    """
    L = [1]
    I = iter(L)                               # Obtain an iterator object from an iterable
    print('I.__next__() = ', I.__next__())    # Call iterator's next to advance to next item
    # I.__next__()                              # Will raise StopIteration exception
    print('iter(L).__next__() = ', iter(L).__next__())    # New iterator on the same list object
    print('iter(range(5)).__next__() = ', iter(range(5)).__next__())


def comprehensions():
    """List comprehensions can be used to iterate over any iterable object. Both set and dictionary comprehensions support the extended syntax of list comprehensions."""

    print([c * 2 for c in 'spam'])                                          # Repeat characters in a string
    print([[x, x / 2, x * 2] for x in range(5) if x % 2 == 0])              # if clause
    print([x + y + z for x in 'abc' for y in 'lmn' for z in 'xyz'])         # nested for loops

    list_of_lines = ['line1', 'line2', 'filterOut']
    print('Set = ', {line for line in list_of_lines if line[0] == 'l'})
    print('Dict = ', {ix: line for ix, line in enumerate(list_of_lines) if line[0] == 'l'})


def looping_functions():
    """Loop Coding Techniques - range, zip, enumerate"""

    for i in range(-6, 6, 2): print(i, 'Pythons')     # range is an iterable that generates items on demand

    L1 = [1, 2, 3, 4, 99]
    L2 = [5, 6, 7, 8]
    # zip takes one or more sequences as arguments and returns a series of tuples that pair up parallel items taken from those sequences.
    # zip truncates result tuples at the length of the shortest sequence when the argument lengths differ
    print('zip result = ', list(zip(L1, L2)))       # Truncates at len(shortest)

    for (offset, item) in enumerate(['a', 'b', 'c']):        # enumerate's net effect is to give loops a counter “for free” by returning an (index, value) tuple each time through the loop
        print(item, ' appears at position ', offset)

    print("next(enumerate('s')) = ", next(enumerate('s')))

    X, Y = (1, 2), (3, 4)
    A, B = zip(*zip(X, Y))
    print('A = {}, B = {}'.format(A, B))


def useful_lib_functions():
    """map(), filter(), min(), max(), any(), all(). map, zip, and filter are their own iterators — after you step through their results once, they are exhausted."""

    L = ['a', 'b']
    strMap = map(str.upper, L)
    print(strMap.__next__())                 # map is itself an iterable in 3.X
    print(list(strMap))

    print(list(filter(bool, ['3', '', '1'])))       # nonempty=True
    print(sum([3, 2, 4, 1, 5, 0]))
    print(max([3, 2, 4, 1, 5, 0]))
    print(min([3, 2, 4, 1, 5, 0]))
    # the any and all built-ins return True if any or all items in an iterable are True
    print(any(['spam', '', 'ni']))
    print(all(['spam', '', 'ni']))


def demo():
    truthiness()
    control_statements()
    iteration_protocol()
    comprehensions()
    looping_functions()
    useful_lib_functions()
