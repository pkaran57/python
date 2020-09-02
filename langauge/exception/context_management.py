"""
with expression [as variable]:
    with-block

The expression here is assumed to return an object that supports the context management protocol (more on this
protocol in a moment). This object may also return a value that will be assigned to the name variable if the optional
as clause is present. Note that the variable is not necessarily assigned the result of the expression; the result of
the expression is the object that supports the context protocol, and the variable may be assigned something else
intended to be used inside the statement.

The object returned by the expression may then run startup code before the with-block is started, as well as
termination code after the block is done, regardless of whether the block raised an exception or not.

Here’s how the with statement actually works:

1. The expression is evaluated, resulting in an object known as a context manager that must have __enter__ and __exit__ methods.
2. The context manager’s __enter__ method is called. The value it returns is assigned to the variable in the as clause if present, or simply discarded otherwise.
3. The code in the nested with block is executed.
4. If the with block raises an exception, the __exit__(type, value, traceback) method is called with the exception details. These are the same three values returned by sys.exc_info,
described in the Python manuals and later in this part of the book. If this method returns a false value, the exception is reraised; otherwise, the exception is terminated. The exception
should normally be reraised so that it is propagated outside the with statement.
5. If the with block does not raise an exception, the __exit__ method is still called, but its type, value, and traceback arguments are all passed in as None.
"""
import os
from contextlib import contextmanager

from langauge.definitions import ROOT_DIR


class TraceBlock:
    def message(self, arg):
        print('running ' + arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            # deleting the return statement would have the same effect, as the default None return value of functions is False by definition
            return True  # Swallow exception for the sake of demo so that demo does not crash


def demo():
    # The with/as statement runs an object’s context management logic to guarantee that termination actions occur,
    # irrespective of any exceptions in its nested block Although file objects may be automatically closed on garbage
    # collection, it’s not always straightforward to know when that will occur, especially when using alternative
    # Python implementations.
    with open(os.path.join(ROOT_DIR, 'data/lumberjack.txt'), 'w') as file:  # Always close file on exit
        file.write('The larch!\n')

    # Multiple Context Managers
    with open(os.path.join(ROOT_DIR, 'data/lumberjack-1.txt'), 'w') as file1, \
            open(os.path.join(ROOT_DIR, 'data/lumberjack-2.txt'), 'w') as file2:  # Always close file on exit
        file1.write('The larch!\n')
        file2.write('The larch!\n')

    with TraceBlock() as action:
        action.message('test 1')
        print('reached')

    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')

    # method below is similar to class TraceBlock
    @contextmanager
    def message():
        print('Get resource as one would in def __enter__(self)')

        def message(arg):
            print('running ' + arg)

        resource = message
        try:
            yield resource
        finally:
            print('Release resource here')

    with message() as resource:
        resource("test")


demo()
