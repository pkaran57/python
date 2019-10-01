"""
try/except
Catch and recover from exceptions raised by Python, or by you.

try/finally
Perform cleanup actions, whether exceptions occur or not.

raise
Trigger an exception manually in your code.

assert
Conditionally trigger an exception in your code.

with/as
Implement context managers in Python 2.6, 3.0, and later (optional in 2.5).
"""


class CustomUserException(Exception):    # User-defined exception
    def __str__(self): return 'Custom error message'


def demo():
    try:
        int('XYZ')
    except:
        print('XYZ is not an int!')
    else:
        print('This will run if no exception raised')

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
