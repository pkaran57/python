# The def statement creates a function object and assigns it to a name. If return is omitted or if return has no value, None is returned
# def is a true executable statement: when it runs, it creates a new function object and assigns it to a name
import builtins


def hello_world_main():
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
    Y= 9
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
