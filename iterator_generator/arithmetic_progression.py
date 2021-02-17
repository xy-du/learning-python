# Iteration pattern is about traversal, but it's not limited to data collection,
# it's also useful when to data items are produced on the fly

# eg.
# range built-in generates a bounded arithmetic progression (AP) of integers
# the itertools.count function generates a boundless AP

class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        # coerce the the type of the result to the type of the subsequence additions
        result = type(self.begin + self.step)(self.begin)
        limitless = self.end is None
        index = 0
        while limitless or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index  # use this 'idiotic' way to reduce the cumulative error


# if your while point is to implement __iter__ to build a generator,
# the whole class can be reduced to a generator function
def aritprog_gen(begin, step, end=None):
    limitless = end is None
    result = type(begin + step)(begin)
    index = 0
    while limitless or result < end:
        yield result
        index += 1
        result = begin + step * index


import itertools


# AP in itertools
def aritprog_gen_its(begin, step, end=None):
    begin = type(begin + step)(begin)
    gen = itertools.count(begin, step)  # itertools.count never stops
    if end is not None:
        gen = itertools.takewhile(lambda n: n < end, gen)
    return gen


if __name__ == '__main__':
    ap = ArithmeticProgression(0, 1, 3)
    print(list(ap))
    ap = ArithmeticProgression(1, .5, 3)
    print(list(ap))
    ap = ArithmeticProgression(0, 1 / 3, 1)
    print(list(ap))
    from fractions import Fraction

    ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    print(list(ap))
    from decimal import Decimal

    ap = ArithmeticProgression(0, Decimal('.1'), .3)
    print(list(ap))

    # the test of the generator function version
    ap = aritprog_gen(0, Fraction(1, 3), 1)
    print(list(ap))

    # test the AP using itertools
    ap = aritprog_gen_its(0, Fraction(1, 3), 1)
    print(list(ap))
