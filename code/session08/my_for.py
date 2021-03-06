#!/usr/bin/env python

"""
hand writing 'for'
"""

import sys

l = [1,2,3,4,5,]

def my_for(an_iterable, func):
    """
    Emulation of a for loop.

    func() will be called with each item in an_iterable

    :param an_iterable: anything that satisfies the interation protocol

    :param func: a callable -- it will be called, passing in each item in an_iterable.

    """
    # equiv of "for i in l:"
    iterator = l.__iter__()
    while True:
        try:
            i = iterator.next()
        except StopIteration:
            break
        func(i)


if __name__ == "__main__":

    def print_func(x):
        print x

    l = [1,2,3,4,5,]
    my_for(l, print_func)

    t = (3,4,5,6)

    my_for(t, print_func)





