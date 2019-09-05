# Like a def, a lambda expression also introduces a new local scope for the function it creates
def func():
    x = 4
    action = (lambda n: x ** n)  # x remembered from enclosing def
    return action


x = func()
print(x(2))  # Prints 16, 4 ** 2


def makeActions_incorrect():
    acts = []
    for i in range(5):  # Tries to remember each i
        acts.append(lambda x: i ** x)  # But all remember same last i!
    return acts


def makeActions_correct():
    acts = []
    for i in range(5):  # Use defaults instead
        acts.append(lambda x, i=i: i ** x)  # Remember current i
    return acts


for action in zip(makeActions_correct(), makeActions_incorrect()):
    print('correct = {}, incorrect = {}'.format(action[0](2), action[1](2)))

