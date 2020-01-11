def demo():

    tuple_assgn = spam, ham = 'yum', 'YUM'  # Tuple assignment (positional)
    print('tuple assignment - {}, spam - {}, ham - {}'.format(tuple_assgn, spam, ham))

    list_assgn = lam, bam = ['yum', 'YUM']  # List assignment (positional)
    print('list assignment - {}, lam - {}, bam - {}'.format(list_assgn, lam, bam))

    a, b, c, d = 'spam'  # Sequence assignment
    a, *b, c = 'spam'  # Extended sequence unpacking (Python 3.X), wherever the starred name shows up, it will be assigned a list that collects every unassigned name at that position
    print('a = {}, b = {}, c = {}'.format(a, b, c))

    spam = ham = 'lunch'  # Multiple-target assignment
    print('Multiple target assignment, spam = {}, ham = {}'.format(spam, ham))

    # a = 1 and so on, note that set_attr is assigned the set '{1, 2, 3}'
    # Python assigns items in the sequence on the right to variables in the sequence on the left by position, from left to right:
    set_attr = a, *b, c = {1, 2, 3, 4}    # set assignment
    print('set = ', set_attr)
    print('a = {}, b = {}, c = {}'.format(a, b, c))

    string = (a, b, c) = "ABC"  # a = A and so on,  string assignment
    print('string = ', string)
    print('a = {}, b = {}, c = {}'.format(a, b, c))

    for ((a, b), c) in [(('S', 'P'), 'AM')]:
        print('From for loop - a = {}, b = {}, c = {}'.format(a, b, c))

    print('\nEdge Cases  - \n')
    seq = {1, 2, 3, 4}

    a, b, c, *d = seq
    print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d))

    a, b, c, d, *e = seq
    print('a = {}, b = {}, c = {}, d = {}, e = {}'.format(a, b, c, d, e))

    *a, = seq
    print('a = ', a)

    # a, *b, c, *d = seq        SyntaxError: two starred expressions in assignment
    # a, b = seq                ValueError: too many values to unpack (expected 2)
    # *a = seq                  SyntaxError: starred assignment target must be in a list or tuple_assgn
