# python has two string representation from any object:
#   repr()  the way developer what to see it
#   str()   the way user what to see to

# another two special methods to support alternative representation of objects:
#   __bytes__   used by bytes() to get obj represented by byte sequence
#   __format__  used by built-in function format() and str.format()

import array
import math


class Vector:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)  # catch args error early
        self.y = float(y)

    # used by tuple(), unpacking, iterator args(*Vector_instance)
    # it should return iterator type, so generator expression(genexps) used here
    def __iter__(self):
        return (i for i in (self.x, self.y))

    # make rebuilt possible
    # *self will call the __iter__
    def __repr__(self):
        cls_name = type(self).__name__
        return '{}({!r},{!r})'.format(cls_name, *self)

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # use the __iter__

    def __str__(self):
        # return '({},{})'.format(self.x, self.y)
        return str(tuple(self))

    def __bytes__(self):  # bytes can concatenate
        return bytes([ord(self.typecode)]) + bytes(array.array(self.typecode, self))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == '__main__':
    v = Vector(3.0, 4.0)
    print(v)
    x, y = v
    print(x, y)
    print(repr(v))
    v_clone = eval(repr(v))
    print(v == v_clone)
    print(v)
    byte_rep = bytes(v)
    print(byte_rep)
    print(abs(v))
    print(bool(v))
    v1 = Vector(0, 0)
    print(bool(v1))
