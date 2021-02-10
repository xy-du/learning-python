# you can not overwrite operator for built-in types
# you can not create new operator
# a few operator can not be overload: is, not, or (but the bitwise &, ~, |, can)

# I copy the Vector here for convenience

# add __neg__ and __pos__ into the class so that it will support - and + operator

# fundamental rule of infix operators:
# always return a new object. In other words, do not modify self,
# but create and return a new instance of a suitable type.

# add __add__ and __radd__ to support infix + operator overload
# NOTE:
# Special methods implementing unary or infix operators should never
# change their operands. they are expected  to produce results by creating new objects.
# Only augmented assignment operators may change the first operand(self)

# How infix and the reversed operator work together
#   1.If a has __add__, call a.__add__(b) and return result unless it’s NotImplemented.
#   2. If a doesn’t have __add__, or calling it returns NotImplemented, check if b has
#   __radd__, then call b.__radd__(a) and return result unless it’s NotImplemented.
#   3. If b doesn’t have __radd__, or calling it returns NotImplemented, raise TypeError
#   with an unsupported operand types message.

# Note:
# Do not confuse NotImplemented with NotImplementedError. The first, NotImplemented,
# is a special singleton value that an infix operator special method should return
# to tell the interpreter it cannot handle a given operand. In contrast, NotImplementedError
# is an exception that stub methods in abstract classes raise to warn that they must
# be overwritten by subclasses.

# add __mul__ and __rmul__ to support *


import array
import functools
import itertools
import math
import numbers
import operator
import reprlib


class Vector:
    typecode = 'd'
    shortcut = 'xyzt'

    def __init__(self, component):
        self._component = array.array(self.typecode, component)

    def __iter__(self):
        return iter(self._component)

    def __repr__(self):
        cls_name = type(self).__name__
        comp_rep = reprlib.repr(self._component)
        comp_rep = comp_rep[
                   comp_rep.find('['):-1]
        return f'{cls_name}({comp_rep})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._component)

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(c) for c in self._component)
        return functools.reduce(operator.xor, hashes, 0)  # give reduce an initializer in case the hashes is empty

    def __abs__(self):
        return math.sqrt(sum(i * i for i in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    # def __add__(self, other):
    #     pairs = itertools.zip_longest(self, other, fillvalue=0.0)
    #     return Vector(x + y for x, y in pairs)

    # base on the rule python use concerning infix operator
    #   returning NotImplemented, you leave the door open for the implementer
    # of the other operand type to perform the operation when Python tries
    # the reversed method call.
    #   And in the spirit of duck typing, we will refrain from testing the type of
    #   the other operand, or the type of its elements. We’ll catch the exceptions
    #   and return NotImplemented.
    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(x + y for x, y in pairs)
        except TypeError:
            return NotImplemented

    # this is called 'reversed' or 'reflected' version of __add__
    # Often, __radd__ can be as simple as that:
    # just invoke the proper operator, therefore
    # delegating to __add__ in this case
    def __radd__(self, other):
        return self + other

    # we could use duck typing like what we do with __add__,
    # no type check, just try catch the error
    # but here we do it in a more explicit way that makes sense in this
    # situation: goose typing.
    # instead of hardcoding some concrete types, we check against the numbers.Real ABC,
    # which covers all the types we need, and keeps our implementation open to future
    # numeric types that declare themselves actual or virtual subclasses of the numbers.Real ABC.
    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(scalar * v for v in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._component)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],
                                     self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._component[item])
        elif isinstance(item, numbers.Integral):
            return self._component[item]
        else:
            raise TypeError(f'{cls.__name__} indices must be integers')

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut.find(item)
            if 0 <= pos < len(cls.shortcut):
                return self._component[pos]
        raise AttributeError(f'{cls.__name__!r} has no attribute {item!r}')

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = "can not set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(attr_name=key, cls_name=cls)
                raise AttributeError(msg)
        super().__setattr__(key, value)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        mem = memoryview(octets[:-1]).cast(typecode)
        return cls(mem)


if __name__ == '__main__':
    v1 = Vector([1, 2, 3])
    print(id(v1), v1)
    v2 = -v1
    print(id(v2), v2)
    v3 = +v1
    print(id(v3), v3)

    # test about + operator
    v4 = v1 + v3
    print(v4)
    v5 = Vector([1, 2, 3, 4])
    v6 = Vector([5, 6, 7])
    print(v5 + v6)

    l = [1, 2, 3]
    # it works with different type
    print(v6 + l)
    # but if we switch the order, and with only __add__
    # TypeError: can only concatenate list (not "Vector") to list
    # that is why need __radd__
    print(l + v6)

    # without the 'try-except' version of __add__, the following two
    # operator will show message that is not help or 'vector-native'
    # TypeError: 'int' object is not iterable
    # after implement the 'try-except' version of __add__, error msg change to
    # TypeError: unsupported operand type(s) for +: 'Vector' and 'int'
    # see the detail reason at the  comment at new version of __add__
    ############################ run in python console###################
    # print(v6 + 1)

    # TypeError: unsupported operand type(s) for +: 'float' and 'str'
    # after implement the 'try-except' version of __add__, error msg change to
    # TypeError: unsupported operand type(s) for +: 'Vector' and 'str'
    ############################ run in python console###################
    # print(v6 + 'ABC')

    # test * operator
    print(v6 * 2)
    print(3 * v6)
    print(True * v6)
    from fractions import Fraction

    print(Fraction(1, 3) * v6)
