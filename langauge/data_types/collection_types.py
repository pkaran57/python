"""
The collections module provides more specialized, high-performance alternatives for the built-in data types as well as a utility function to create named tuples. The following table lists the datatypes and operations of the collections module and their descriptions:

namedtuple()- factory function for creating tuple subclasses with named fields
deque- list-like container with fast appends and pops on either end
ChainMap- dict-like class for creating a single view of multiple mappings
Counter- dict subclass for counting hashable objects
OrderedDict- dict subclass that remembers the order entries were added
defaultdict- dict subclass that calls a factory function to supply missing values
UserDict- wrapper around dictionary objects for easier dict subclassing
UserList- wrapper around list objects for easier list subclassing
UserString- wrapper around string objects for easier string subclassing
"""
from collections import namedtuple


def list_type():
    """Lists - Lists are positionally ordered collections of arbitrarily typed objects, and they have no fixed size. They are also mutable"""

    L = [123, 'spam', 1.23]            # A list of three different-type objects
    print(L[:-1])
    print(L + [4, 5, 6])        # new list will be created
    print(L * 2)

    L.append('NI')                     # Growing: add object at end of list
    L.pop(2)                           # Shrinking: delete an item in the middle

    print('L = ', L)

    L = [1, 2, 6, 0]
    L.sort()
    L.reverse()

    L = [1, 2, 3]
    L += 'abc'          # += allows arbitrary sequences (just like extend)
    print('L = ', L)
    # L = L + 'spam'      # this will result into an error - TypeError: can only concatenate list (not "str") to list

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
    print('Diagonal = ', [M[i][i] for i in range(len(M))])


def dictionaries_type():
    """Dictionaries - consist of a series of “key: value” pairs"""

    D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
    print(D['quantity'])
    D['newKey'] = 'newValue'
    D['quantity'] += 1
    print(D)
    print(dict(name={'nested': 'dictionary'}, job='dev', age=40)['name'])
    print(dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])))

    print('f' in D)     # check if a key is in dictionary
    print(D.get('f', 'default'))


def tuple_type():
    """Tuples - roughly like a list that cannot be changed—tuples are sequences, like lists, but they are immutable, like strings"""

    T = (1, 2, 3, 4)
    print(T + (5, 6))
    print(T[0])
    # T[0] = 99    Tuples are immutable, cannot do this!
    T = 'spam', 3.0, [11, 22, 33]       # another way of creating a tuple, np params needed!
    print('Tuple comprehension statement - ', tuple(i for i in [1, 2, 3]))
    print('type of data struct = ', type(tuple((i for i in [5, 6, 7]))))


def set_type():
    print("set() = ", set())       # {} is an empty dictionary, use set() to create an empty set
    X = set('spam')
    Y = {'h', 'a', 'm'}
    print(X, Y)    # tuple of two sets
    print(X & Y)   # Intersection
    print(X | Y)   # Union
    print(X - Y)   # Difference
    print(X > Y)   # Superset
    print({n ** 2 for n in [1, 2, 3, 4]})   # Set comprehension
    print("set('spam') == set('asmp') = ", set('spam') == set('asmp'))      # Order-neutral equality
    print("'p' in set('spam') = ", 'p' in set('spam')) # in membership test


def named_tuples():
    """
    If we do not need to add behavior to the object, and we know in advance which attributes we need to store,
    we can use a named tuple. They are a great way to group read-only data together.
    """

    '''Describe the named tuple by giving it a name and outlining its attributes. This returns a class-like object 
    that we can instantiate with the required values as many times as we want. The namedtuple constructor accepts two 
    arguments. The first is an identifier for the named tuple. The second is a list of string attributes that the 
    named tuple requires. The result is an object that can be called just like a normal class to instantiate other 
    objects. The constructor must have exactly the correct number of arguments that can be passed in as arguments or 
    keyword arguments. '''

    Stock = namedtuple("Stock", ["symbol", "current", "high", "low"])
    stock = Stock("FB", 177.46, high=178.67, low=175.79)

    print(stock.current)

    symbol, current, high, low = stock
    print(symbol)
    print(stock[0])

def demo():
    list_type()
    dictionaries_type()
    tuple_type()
    set_type()
    named_tuples()
