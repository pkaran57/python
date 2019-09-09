# The def statement creates a function object and assigns it to a name. If return is omitted or if return has no value, None is returned
# def is a true executable statement: when it runs, it creates a new function object and assigns it to a name
import builtins
import sys


# function annotations — arbitrary user-defined data about a function’s arguments and result—to a function object.
# Annotations are simply attached to the function object’s __annotations__ attribute for use by other tools. For instance, such a tool might use annotations in the context of error testing.
def hello_world_main(a:'annotation to a parameter'= 9, b:bool=True) -> 'return value annotation':             # when the def is done running, hello_world_main variable gets assigned the function object
    test = None
    if test:
        def hello_world():
            print("Hello World true!")
    else:
        def hello_world():
            print("Hello World false!")
    return hello_world()


function_object = hello_world_main
function_object()
function_object.test = True  # functions allow arbitrary attributes to be attached to record information for later use

print('hello_world_main function annotations - ', hello_world_main.__annotations__)     # function annotations stored inside a dictionary

# polymorphism - meaning of an operation depends on the objects being operated upon. Example x + y where x and y are strings vs numbers
def polymorphism(x, y):
    return x + y


print('polymorphism(1,2) = ', polymorphism(1, 2))
print("polymorphism('a', 'b') = ", polymorphism('a', 'b'))

x = 'variable in global scope'  # scope of this variable is specific to this module file


# Assigned names within functions are in local scope (specific to the function) unless declared global or nonlocal
def intersect(seq1, seq2):
    """The intersect method uses polymorphism to find common items between two sequences."""

    set = {x for x in seq1 if x in seq2}
    print(x)  # scope of x is specific to the set comprehension above
    return set


print(intersect('test', 'jest'))
print(intersect([1, 2, 3], [3, 4, 5]))

seq1 = zip((1, 2, 3), (4, 5, 6))
seq2 = [(1, 4), (2, 5), (3, 6)]
print(intersect(seq1, seq2))


def return_tuple():
    return 1, [2, 3]  # returns tuple, tuple variable assignment at play


a, b = return_tuple()
print('Items returned by function as tuple = {}, {}'.format(a, b))

''' Arguments

By default, arguments are matched by position, from left to right, and you must pass exactly as many arguments as there are argument names in the function header. However, you can also specify matching by name, provide default values, and use collectors for extra arguments.

If you choose to use and combine the special argument-matching modes, Python will ask you to follow these ordering rules among the modes’ optional components:

* In a function call, arguments must appear in this order: any positional arguments (value); followed by a combination of any keyword arguments (name=value) and the *iterable form; followed by the **dict form.
* In a function header, arguments must appear in this order: any normal arguments (name); followed by any default arguments (name=value); followed by the *name (or * in 3.X) form; followed by any name or name=value keyword-only arguments (in 3.X); followed by the **name form.

The steps that Python internally carries out to match arguments before assignment can roughly be described as follows:
1. Assign nonkeyword arguments by position.
2. Assign keyword arguments by matching names.
3. Assign extra nonkeyword arguments to *name tuple.
4. Assign extra keyword arguments to **name dictionary.
5. Assign default values to unassigned arguments in header.
After this, Python checks to make sure each argument is passed just one value; if not, an error is raised. When all matching is complete, Python assigns argument names to the objects passed to them.
'''


def f(a, b=[77, 88], c=99, modify_b=False):
    print('f(a,b,c) = ', a, b, c)  # 99 is default for c
    if (modify_b): b[1] = 55


f(1, 2, 3)
f(c=3, b=2, a=1)
f(1, c=3, b=2)  # a gets 1 by position, b and c passed by name
f(1, 2)
f(1, c=2)  # b is the default one

f(2, modify_b=True)
# argument’s default retains its value from the prior call, and is not reset to its original value coded in the def header. To reset anew on each call, move the assignment into the function body instead.
f(3)


def tup(*args): print('tup() = ',args)  # Python collects all the positional arguments into a new tuple and assigns the variable args to that tuple
tup()
tup(1)
tup(1, 2, 3, 4, 5)


# The ** feature is similar, but it only works for keyword arguments—it collects them into a new dictionary, which can then be processed with normal dictionary tools
def dict(**args): print('dict() = ',args)
dict()
# dict(1,2)     # Will throw TypeError: dict() takes 0 positional arguments but 2 were given
dict(a=1, b=2)


def mix(a, *pargs, **kargs): print('mix() = ', a, pargs, kargs, sep=', ')
mix(1, 2, 3, x=1, y=2)

# *pargs form in a call is an iteration context, so technically it accepts any iterable object.  For instance, a file object works after the *, and unpacks its lines into individual arguments (e.g., func(*open('fname'))
f(*(22, 33, 44))        # UNPACKING tuple
f(*[22, 33, 44])        # UNPACKING list

f(**{'c': 22, 'a': 33, 'b': 44})        # UNPACKING dictionary, note that using ** instead of *

# keyword-only arguments are coded as named arguments that may appear after *args in the arguments list. All such arguments must be passed using keyword syntax in the call.
def kwonly(a, *b, c):
    print(a, b, c)

kwonly(a=1, c=3)
# kwonly(1, 2, 3)            # TypeError: kwonly() missing 1 required keyword-only argument: 'c'

# We can also use a * character by itself in the arguments list to indicate that a function does not accept a variable-length argument list but still expects all arguments following the * to be passed as keywords.
def kwonly(a, *, b, c, d= 99):
    print(a, b, c, d)

kwonly(1, b=1, c=1)     # keyword-only arguments with defaults are optional
# kwonly(1, 2, 3)            # TypeError: kwonly() missing 2 required keyword-only arguments: 'b' and 'c'

''' 4 scopes in Python:
1. Built-in - Names in the built-in module (ex: open, range)
2. Global (module) - All the names assigend at top level of a module file, or declared global in a def within a file
3. Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer
4. Local (function) - Names assigned in any way within a function (def or lambda), and not declared global in that function

 LEGB rule - When you use an unqualified name inside a function, Python searches up to four scopes—the local (L) scope, then the local scopes of any enclosing (E) defs and lambdas, then the global (G) scope, and then the built-in (B) scope—and stops at the first place the name is found. If the name is not found during this search, Python reports an error.
'''

print('All the names in the built-in scope - ', dir(builtins))

X = 88


def func():
    global X  # global statement tells Python that a function plans to change one or more global names
    global Y
    Y = 9
    X = 99  # Local X: hides global, but we want this here


func()
print(X)  # Prints 99, but only if func() is called!
print("var Y in global scope (even if defined within function body) = ", Y)


# nonlocal allows a nested function to change one or more names defined in a syntactically enclosing function’s scope.
def non_local_demo(start_value):
    var_in_function_scope = start_value

    def enclosed_function():
        nonlocal var_in_function_scope
        var_in_function_scope += 1
        return var_in_function_scope

    enclosed_function.func_attr = 'This is a function attribute!'
    return enclosed_function


# nonlocals are per-call, i.e. each instance of the nonlocaldemo function object will have its own copy of `var_in_function_scope`
# nonlocal restricts scope lookup to just enclosing defs, requires that the names already exist there, and allows them to be assigned. Scope lookup does not continue on to the global or built-in scopes
# It addresses simple state-retention needs where classes may not be warranted and global variables do not apply, though function attributes can often serve similar roles more portably
func_1 = non_local_demo(0)
func_2 = non_local_demo(5)

# print('nonlocal names are still not visible outside the enclosing function', func_1.var_in_function_scope)        # will throw AttributeError: 'function' object has no attribute 'var_in_function_scope'
print('function attribute - ', func_1.func_attr)
print('invocation #1 = {}, #2 = {}'.format(func_1(), func_1()))
print('invocation #1 = {}, #2 = {}'.format(func_2(), func_2()))


# recursion
def mysum(L): return 0 if not L else L[0] + mysum(L[1:])

print('Sum = ', mysum([1,2,3]))
print(sys.getrecursionlimit())          # max stack depth
print(help(sys.setrecursionlimit))
