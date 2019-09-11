"""
Generators - generators can be better in terms of both memory use and performance in larger programs. They allow functions to avoid doing all the work up front,
which is especially useful when the result lists are large or when it takes a lot of computation to produce each value. Generators distribute the time required
to produce the series of values among loop iterations.

Generator function - A function def statement that contains a yield statement is turned into a generator function. When called, it returns a new generator object with
automatic retention of local scope and code position; an automatically created __iter__ method that simply returns itself; and an automatically created __next__ method (next in 2.X)
that starts the function or resumes it where it last left off, and raises StopIteration when finished producing results.

Generator expression - A comprehension expression enclosed in parentheses is known as a generator expression. When run, it returns a new generator object with the same
automatically created method interface and state retention as a generator function call’s results—with an __iter__ method that simply returns itself; and a _next__ method (next in 2.X)
that starts the implied loop or resumes it where it last left off, and raises StopIteration when finished producing results.
"""

# generator function
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

#
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