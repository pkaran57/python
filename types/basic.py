"""
Build-In Data Types - Everything is an object in Python

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

import decimal
import math
import random
from decimal import Decimal
from fractions import Fraction


def demo():
    numbers()
    string()
    others()


demo()


def numbers():
    """
    Python’s core objects set includes the usual suspects: integers that have no fractional part, floating-point numbers that do, and more exotic types—complex numbers with imaginary parts,
    decimals with fixed precision, rationals with numerator and denominator, and full-featured sets.
    """

    print('integer = ', 999999)  # unlimited size

    # Floating-point numbers have a decimal point and/or an optional signed exponent introduced by an e or E and followed by an optional sign
    #  Floating-point numbers are implemented as C “doubles” in standard CPython, and therefore get as much precision as the C compiler used to build the Python interpreter
    print('float = ', -3.14e-10)

    # Decimal -  decimals are fixed-precision floating-point values
    # When decimals of different precision are mixed in expressions, Python converts up to the largest number of decimal digits automatically. For below, answer will be 0.00

    print("Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') = ", Decimal('0.10') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
    print(" decimal.Decimal(1) / decimal.Decimal(7) = ", Decimal(1) / Decimal(7))
    decimal.getcontext().prec = 2  # The precision is applied globally for all decimals created in the calling thread
    print(" decimal.Decimal(1) / decimal.Decimal(7) = ", Decimal(1) / Decimal(7))

    # Fractions - Fraction is a functional cousin to the Decimal fixed-precision type described in the prior section, as both can be used to address the floating-point type’s numerical inaccuracies.
    print("Fraction(2, 3) = ", Fraction(2, 3))
    print("Fraction('.25') = ", Fraction('.25'))

    # MIXED TYPES ARE CONVERTED UP - integers are simpler than floating-point numbers, which are simpler than complex numbers
    print('40 + 3.13 = ', 40 + 3.13)

    print('int(-3.14) = ', int(-3.14))  # Truncates float to integer

    random.random()
    math.sqrt(85)


def string():
    """Strings are sequences of one-character strings; other, more general sequence types include lists and tuples, covered later """

    S = '''
    All the lines are concatenated together, 
    and end-of-line characters are added where line breaks appear.
    '''
    print(S)
    print('Raw bytes - {}, str type - {}'.format(b'sp\xc4m', 'sp\xc4m'))   # In Python 3.X, the normal str string handles Unicode text, a distinct bytes string type represents raw byte values

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


def others():
    """Other types"""

    print(True, False)  # True and False objects that are essentially just the integers 1 and 0 with custom display logic
    print(None)         # special placeholder object called None commonly used to initialize names and objects
    L = ['This', 'is', 'a', 'list']
    print(type(L))      # The type object, returned by the type built-in function, is an object that gives the type of another object
    print(type(type(L)))
