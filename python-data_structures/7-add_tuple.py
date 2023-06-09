#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        # potential cause of the problem because it might not be adding each
        # one independently
        new_tuple = list(map(lambda y: 0 + y, tuple_b))
    elif len(tuple_b) < 2:
        new_tuple = list(map(lambda x: x + 0, tuple_a))
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        for i in len(tuple_b) < 2:
            new_tuple = tuple_a[i] + tuple_b[i]
    else:
        new_tuple = list(map(lambda x, y: x + y, tuple_a, tuple_b))
    return (new_tuple)
