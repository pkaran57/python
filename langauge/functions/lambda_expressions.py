# lambdas are un-named functions, its form : lambda argument1, argument2,... argumentN : expression using arguments

# lambda’s body is a single expression, not a block of statements
import functools
import operator


def demo():
    lambda_function = lambda a, b, c=3: a + b + c           # default arguments work with lambdas
    print('lambda_function = ', lambda_function(1, 2))

    # Like a def, a lambda expression also introduces a new local scope for the function it creates. The code in a lambda body also follows the same scope lookup rules as code inside a def.
    def func():
        x = 4
        action = lambda n: x ** n  # x remembered from enclosing def
        return action


    x = func()
    print(x(2))  # Prints 16, 4 ** 2


    def make_actions_incorrect():
        acts = []
        for i in range(5):  # Tries to remember each i
            acts.append(lambda x: i ** x)  # But all remember same last i!
        return acts


    def make_actions_correct():
        acts = []
        for i in range(5):  # Use defaults instead
            acts.append(lambda x, i=i: i ** x)  # Remember current i
        return acts


    for action in zip(make_actions_correct(), make_actions_incorrect()):
        print('correct = {}, incorrect = {}'.format(action[0](2), action[1](2)))


    # Functional Programming Tools
    print('map = ', list(map(lambda x: x + 1, [1, 2, 3])))
    print('map 2 = ', list(map(pow, [1, 2, 3], [2, 3, 4])))          # given multiple sequence arguments, it sends items taken from sequences in parallel as distinct arguments to the function. pow(x, y)

    print('filter = ', list(filter(lambda x: x >= 0, (-1, -2, -3, 0, 1, 2, 3))))

    print('reduce - ', functools.reduce(operator.add, [1, 2, 3]))       # operator module provides functions that correspond to built-in expressions
