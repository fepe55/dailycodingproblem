"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
and last element of that pair.
For example,
car(cons(3, 4)) returns 3,
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair_f):
    return pair_f(lambda a, _: a)


def cdr(pair_f):
    # return pair_f(lambda _, b: b)
    def get_last(a, b):
        return b
    return pair_f(get_last)


if __name__ == '__main__':
    output = car(cons(3, 4))
    print(output == 3)
    output = cdr(cons(3, 4))
    print(output == 4)
