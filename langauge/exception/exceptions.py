"""
* Keywords:

try/except
Catch and recover from exceptions raised by Python, or by you.

try/finally
Perform cleanup actions, whether exceptions occur or not.

raise
Trigger an exception manually in your code.

assert
Conditionally trigger an exception in your code.

As an added feature, assert statements may be removed from a compiled program’s byte code if the -O Python command-line flag is used, thereby optimizing the program.
AssertionError is a built-in exception, and the __debug__ flag is a built-in name that is automatically set to True unless the -O flag is used. Use a command line like python –O main.py
to run in optimized mode and disable (and hence skip) asserts.

with/as
Implement context managers in Python 2.6, 3.0, and later (optional in 2.5).

* Different ways of using except:

try:
    statements              # Run this main action first
except name1:
    statements              # Run if name1 is raised during try block
except (name2, name3):
    statements              # Run if any of these exceptions occur
except (name1, name2) as value:
    statements              # Catch any listed exception and assign its instance.
except name4 as var:
    statements              # Run if name4 is raised, assign instance raised to var
except:
    statements              # Run for all other exceptions raised
except Exception:
    statements              # Catch all possible exceptions, except exits
else:
    statements              # Run if no exception was raised during try block. Can only use one else when except is present
finally:
    statements              # Always perform this block on exit. Can only use one finally

* Different ways of using raise:

raise instance               # Raise instance of class
raise class                  # Make and raise instance of class: makes an instance
raise                        # Reraise the most recent exception, it’s commonly used in exception handlers to propagate exceptions that have been caught.
"""


class CustomUserException(Exception):    # User-defined exception
    def __str__(self): return 'Custom error message'


def demo():
    X = 99
    try:
        int('XYZ')
    except ValueError as X:                         # Python 3.X localizes the exception reference name (X) to the except block. NOTE : the variable is not available after the block exits!
        print('XYZ is not an int!', X)
    else:
        print('This will run if no exception raised')

    # print(X)        # UnboundLocalError: local variable 'X' referenced before assignment

    try:
        raise CustomUserException
    except CustomUserException:
        print('Caught an error that was raised in the try block!')

    try:
        assert False, 'Nobody expects the Spanish Inquisition!'     # assertions will raise exceptions during debugging (turned on via a flag)
    except:
        print('Error from assertion failure!')
    finally:
        print('finally executes no matter what!')

    # The with/as statement runs an object’s context management logic to guarantee that termination actions occur, irrespective of any exceptions in its nested block
    with open('data/lumberjack.txt', 'w') as file:        # Always close file on exit
        file.write('The larch!\n')

    try:
        1/0
    except Exception as E:
        # Explicitly chained exceptions, the expression following from specifies another exception class or instance to attach to the __cause__ attribute of the new exception being raised
        # raise TypeError('Bad') from E
        pass

    # When an exception is raised implicitly by a program error inside an exception handler, a similar procedure is followed automatically: the previous exception is attached to the new exception’s
    # __context__ attribute and is again displayed in the standard error message if the exception goes uncaught:
    try:
        1 / 0
    except:
        pass
        # badname                                    # Implicitly chained exceptions
