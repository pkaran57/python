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

# Loop Coding Techniques - range, zip, enumerate
for i in range(-6, 6, 2):
    print(i, 'Pythons')     # range is an iterable that generates items on demand

L1 = [1, 2, 3, 4, 99]
L2 = [5, 6, 7, 8]
# zip takes one or more sequences as arguments and returns a series of tuples that pair up parallel items taken from those sequences.
# zip truncates result tuples at the length of the shortest sequence when the argument lengths differ
print('zip result = ', list(zip(L1, L2)))       # Truncates at len(shortest)


for (offset, item) in enumerate(['a', 'b', 'c']):        # enumerate's net effect is to give loops a counter “for free” by returning an (index, value) tuple each time through the loop
    print(item, ' appears at position ', offset)

print("next(enumerate('s')) = ", next(enumerate('s')))

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

# List comprehensions can be used to iterate over any iterable object

print([c * 2 for c in 'spam'])                      # Repeat characters in a string
print([[x, x / 2, x * 2] for x in range(5) if x % 2 == 0])              # if clause
print([x + y + z for x in 'abc' for y in 'lmn' for z in 'xyz'])         # nested for loops

# both set and dictionary comprehensions support the extended syntax of list comprehensions
listOfLines = ['line1', 'line2', 'filterOut']
print('Set = ', {line for line in listOfLines if line[0] == 'l'})
print('Dict = ', {ix: line for ix, line in enumerate(listOfLines) if line[0] == 'l'})

# map(), filter(), min(), max(), any(), all()
# map, zip, and filter are their own iterators — after you step through their results once, they are exhausted

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

# '*arg' form can be used in function calls to unpack a collection of values into individual arguments
def f(a, b, c, d): print(a, b, c, d, sep='&')
f(*[1, 2, 3, 4])

X = (1, 2)
Y = (3, 4)

A, B = zip(*zip(X, Y))
print('A = {}, B = {}'.format(A, B))

# Generators - generators can be better in terms of both memory use and performance in larger programs. They allow functions to avoid doing all the work up front, which is especially useful when the result lists are large
# or when it takes a lot of computation to produce each value. Generators distribute the time required to produce the series of values among loop iterations.

# Generator function - A function def statement that contains a yield statement is turned into a generator function. When called, it returns a new generator object with automatic retention of local scope and code position; an automatically created __iter__ method that simply returns itself; and an automatically created __next__ method (next in 2.X) that starts the function or resumes it where it last left off, and raises StopIteration when finished producing results.

def generator(N):
    for i in range(N):      # state of range(N) will be preserved between function calls
        # The yield statement suspends function’s execution and sends a value back to caller, but retains enough state to enable function to resume where it is left off.
        # When resumed, the function continues execution immediately after the last yield run.
        yield i ** 2        # To end the generation of values, functions either use a return statement with no value or simply allow control to fall off the end of the function body.

for i in generator(5): print('generator return value = ', i)

# You get back a generator object that supports the iteration protocol
# The returned generator object in turn has a __next__ method that starts the function or resumes it from where it last yielded a value, and raises a StopIteration exception when the end of the series of values is reached and the function returns.
print('generator object is returned in case of a yield in the function - ', generator(1))

generator_instance = generator(2)
print(iter(generator_instance) is generator_instance)  # iter() is not required: a no-op here

print('next = ', next(generator_instance))
print('next = ', next(generator_instance))
# next(generator_instance)              # will throw StopIteration error as per Python's iteration protocol

# The send method advances to the next item in the series of results, just like __next__, but also provides a way for the caller to communicate with the generator, to affect its operation.
def gen():
    for i in range(10):
        X = yield i         # the yield expression in the generator returns the value passed to send, If the regular G.__next__() method (or its next(G) equivalent) is called to advance, the yield simply returns None.
        print(X)

G = gen()
print(next(G))
print(G.send(78))
print(next(G))

# GENERATOR EXPRESSIONS - A comprehension expression enclosed in parentheses is known as a generator expression. When run, it returns a new generator object with the same automatically created method interface and state retention as a generator function call’s results—with an __iter__ method that simply returns itself; and a _next__ method (next in 2.X) that starts the implied loop or resumes it where it last left off, and raises StopIteration when finished producing results.
# Just like generator functions, generator expressions are a memory-space optimization—they do not require the entire result list to be constructed all at once, as the square-bracketed list comprehension does
# generator expressions may also run slightly slower than list comprehensions in practice, so they are probably best used only for very large result sets, or applications that cannot wait for full results generation.
print('expression object returned - ', (x + 1 for x in [1, 2, 3]))     # the expression within the print will return a generator!

# yield from statement - allows delegation to a subgenerator with a from generator clause
def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

print(list(both(4)))

# Comprehending Set and Dictionary Comprehensions
print('set - ', set(x * x for x in range(10)))
print('dictionary - ', dict((x, x * x) for x in range(10)))
