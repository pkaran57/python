# imports must find files, compile them to byte code, and run the code.
import math
import random
import sys                  # Load a library module

import module               # import a module, each module file is a package of variables—that is, a namespace
# commenting out line below so that it does not get removed while optimizing imports
# from module import var1     from copies a module’s attributes, such that they become simple variables in the recipient

var1 = "This will overridden var1 reference by the by the 'import from' statement above!"

print(sys.platform)
print(module.var, var1)

"""
 Data Types
"""

# Numbers - Python’s core objects set includes the usual suspects: integers that have no fractional part, floating-point numbers that do, and more exotic types—complex numbers
# with imaginary parts, decimals with fixed precision, rationals with numerator and denominator, and full-featured sets.

random.random()
math.sqrt(85)

# Strings - Strings are sequences of one-character strings; other, more general sequence types include lists and tuples, covered later.

S = 'Spam'
print(len(S), S[0], S[3], S[-2], S[-1])
print(S[1:], S[0:3], S[:3], S[:-1], S[:])
print(S * 3)

print(S.replace('pa', 'xx'))
print(S)        # Strings are immutable in Python

print('%s, eggs, and %s' % ('spam', 'SPAM!') )         # Formatting expression (all)
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))      # Numbers optional (2.7+, 3.1+)

print(dir(S))   # dir() attempts to return all attributes of this object

# input()
