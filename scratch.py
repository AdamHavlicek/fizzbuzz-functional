# -*- encoding: UTF-8 -*-

class Pair(object):
    __slots__ = ('first', 'second')

    def __init__(self, first, second):
        self.first = first
        self.second = second


def pair(first):
    return lambda second: Pair(first, second)


def head(p):
    """

    :param Pair p:
    """
    return p.first


def tail(p):
    """

    :param Pair p:
    """
    return p.second


def array_to_list(array):
    result = []

    while array is not None:
        result.append(head(xs))
        array = tail(xs)

    return result


def list_to_array(list_like):
    result = None

    for element in reversed(list_like):
        result = pair(element)(result)

    return result


def range(low):
    return lambda high: None if low > high else pair(low)(range(low + 1)(high))


def fizzbuzz(n):
    def fizz():
        return 'Fizz' if n % 3 == 0 else ''

    def buzz():
        return 'Buzz' if n % 5 == 0 else ''

    return fizz() + buzz() or n


def map(f):
    def inner(array):
        return None if array is None else pair(f(head(array)))(map(f)(tail(array)))
    return inner


if __name__ == '__main__':
    my_range = range(1)(100)
    print(array_to_list(map(lambda x: fizzbuzz(x))(my_range)))

    exit(0)
