# The philosophy of the Python data model is to cooperate with essential protocols as much as possible.

# the example below work because of the special treatment Python gives to anything vaguely resembling a sequence.
# Iteration in Python represents an extreme form of duck typing: the interpreter tries two different methods to
# iterate over objects.

class Foo:
    def __getitem__(self, item):
        return range(5)[item]


if __name__ == '__main__':
    f = Foo()
    print(f[2])

    # There is no method __iter__ yet Foo instances are iterable, because—as a fallback— when
    # Python sees a __getitem__ method, it tries to iterate over the object by calling that
    # method with integer indexes starting with 0.
    for i in f:
        print(i)

    # in operator work even if Foo has no __contains__ method:
    # it does a FULL scan to check if an item is present.
    print(2 in f)
