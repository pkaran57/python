def demo():
    x, y = 0, 100

    print("'true' if x else 'false' = ", 'true' if x else 'false')    # x if y else z, Ternary selection (x is evaluated only if y is true)
    print('x or y = ', x or y)          # Logical OR (y is evaluated only if x is false)
    print('x and y = ', x and y)        # Logical AND (y is evaluated only if x is true)
    print('not x = ', not x)
    print('x not in [0, 1] = ', x not in [0, 1])
    x1 = x
    print('x1 is x = ', x1 is x)          # Object identity test
    print('x != 0 - ', x == 0)            # Value equality operators, != and ==
