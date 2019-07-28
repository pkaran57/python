# imports must find files, compile them to byte code, and run the code.
import math
import random
import sys                  # Load a library module

import module               # import a module, each module file is a package of variables—that is, a namespace
# commenting out line below so that it does not get removed while optimizing imports
# from module import var1     from copies a module’s attributes, such that they become simple variables in the recipient

var1 = "This will overridden var1 reference by the by the 'import from' statement above!"

print(sys.platform)
print(module.var1, var1)

aString = ''

print(dir(aString))           # dir() attempts to return all attributes of this object
print(help(aString.replace))  # Get info on a specific attribute
print(dir(str))         # Both dir and help also accept as arguments either a real object (like our string S), or the name of a data type (like str, list, and dict)
print(dir(str.replace))

"""
Build-In Data Types

Numbers - 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
Strings - 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
Lists - [1, [2, 'three'], 4.5], list(range(10))
Dictionaries - {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
Tuples - (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
Files - open('eggs.txt'), open(r'C:\ham.bin', 'wb')
Sets - set('abc'), {'a', 'b', 'c'}
Other core types - Booleans, types, None
Program unit types - Functions, modules, classes (Part IV, Part V, Part VI)
Implementation-related types - Compiled code, stack tracebacks (Part IV, Part VII)
"""

# Numbers - Python’s core objects set includes the usual suspects: integers that have no fractional part, floating-point numbers that do, and more exotic types—complex numbers
# with imaginary parts, decimals with fixed precision, rationals with numerator and denominator, and full-featured sets.

random.random()
math.sqrt(85)

# Strings - Strings are sequences of one-character strings; other, more general sequence types include lists and tuples, covered later.

S = '''
All the lines are concatenated together, 
and end-of-line characters are added where line breaks appear.
'''
print(S)
print('Raw bytes - {}, str type - {}'.format(b'sp\xc4m', 'sp\xc4m'))   # In Python 3.X, the normal str string handles Unicode text, a distinct bytes string type represents raw byte values
# Unicode processing mostly reduces to transferring text data to and from files—text is encoded to bytes when stored in a file, and decoded into characters (a.k.a. code points)
# when read back into memory. Once it is loaded, we usually process text as strings in decoded form only.

S = 'A\nB\tC'            # \n is end-of-line, \t is tab
S = 'Spam'
print(len(S), S[0], S[3], S[-2], S[-1])
print(S[1:], S[0:3], S[:3], S[:-1], S[:])
print(S * 3)

print(S.replace('pa', 'xx'))
print(S)        # Strings are immutable in Python

print('%s, eggs, and %s' % ('spam', 'SPAM!') )         # Formatting expression (all)
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))      # Numbers optional (2.7+, 3.1+)

# Lists - Lists are positionally ordered collections of arbitrarily typed objects, and they have no fixed size. They are also mutable

L = [123, 'spam', 1.23]            # A list of three different-type objects
print(L[:-1])
print(L + [4, 5, 6])
print(L * 2)

L.append('NI')                     # Growing: add object at end of list
L.pop(2)                           # Shrinking: delete an item in the middle

L = [1, 2, 6, 0]
L.sort()
L.reverse()

# Both the statements below will result in an IndexError
# L[99] = 23
# L[99]

M = [[1, 2, 3],               # A 3 × 3 matrix, as nested lists
     [4, 5, 6],               # Code can span lines if bracketed
     [7, 8, 9]]

print(M[0][2])

col2 = [row[1] for row in M]    # list comprehension expression, Give me row[1] for each row in matrix M, in a new list.
print(col2)
print([row[1] + 1 for row in M])                    # Add 1 to each item in column 2
print([row[1] for row in M if row[1] % 2 == 0])     # Filter out odd items
print([M[i][i] for i in [0, 1, 2]])                 # Collect a diagonal from matrix

# List comprehensions can be used to iterate over any iterable object
print([c * 2 for c in 'spam'])                      # Repeat characters in a string
print([i for i in range(3)])        # can also use list(range(3))
# List comprehensions can also be used to collect multiple values, as long as we wrap those values in a nested collection
print([[x, x / 2, x * 2] for x in range(4) if x % 2 == 0])

# Generators using comprehensions - its values aren’t stored in memory all at once, but are produced as requested

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

print(list(map(sum, M)))        # Map sum over items in M

# Dictionaries - consist of a series of “key: value” pairs

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['quantity'])
D['newKey'] = 'newValue'
D['quantity'] += 1
print(D)
print(dict(name={'nested': 'dictionary'}, job='dev', age=40)['name'])
print(dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])))

print('f' in D)     # check if a key is in dictionary
print(D.get('f', 'default'))

# Tuples - roughly like a list that cannot be changed—tuples are sequences, like lists, but they are immutable, like strings

T = (1, 2, 3, 4)
print(T + (5, 6))
print(T[0])
# T[0] = 99    Tuples are immutable, cannot do this!
T = 'spam', 3.0, [11, 22, 33]       # another way of creating a tuple, np params needed!

# Files

f = open('data/data.txt', 'w')       # Make a new file in output mode ('w' is write)
f.write('Hello world!\n')             # Write strings of characters to it
f.close()                      # Close to flush output buffers to disk

f = open('data/data.txt')           # 'r' (read) is the default processing mode
print('Following is the content of the file - \n{}'.format(f.read()))      # Read entire file into a string

