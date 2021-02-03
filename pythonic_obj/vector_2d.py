# python has two string representation from any object:
#   repr()  the way developer what to see it
#   str()   the way user what to see to

# another two special methods to support alternative representation of objects:
#   __bytes__   used by bytes() to get obj represented by byte sequence
#   __format__  used by built-in function format() and str.format()

# when a object can be seen as hashable:
#   support hash() function through hash() method that always return the same value over the lifetime of the
# project
#   it supports eq() method
#   if a==b then hash(a)==hash(b) must also be True
# NOTE:
# if you implement a custom __eq__, then you also have to implement a suitable __hash__, because you have to
# make sure that if a==b is True then hash(a)==hash(b) is also True

# NOTE:
# here I implement a pretty full-fledged object, but it's not necessary and a bad idea to implement all the
# method if you application has no real use of them. Customers don't care if you object are 'Pythonic' or not
import array
import math


class Vector:
    typecode = 'd'

    # def __init__(self, x, y):
    #     self.x = float(x)  # catch args error early
    #     self.y = float(y)
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    # mark the getter method of a property, every method tht reads x,y components can stay as they were
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        mem = memoryview(octets[1:]).cast(typecode)
        return cls(*mem)

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

    # using bitwise XOR operator(^) to mix the hashes of the components is what the document suggests
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __str__(self):
        # return '({},{})'.format(self.x, self.y)
        return str(tuple(self))

    def __bytes__(self):  # bytes can concatenate
        return bytes([ord(self.typecode)]) + bytes(array.array(self.typecode, self))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]  # for str, tuple, this change inplace. for list, this make a new copy
            fmt_out = '<{},{}>'
            mag = abs(self)
            angle = math.atan2(self.x, self.y)
            coord = (mag, angle)  # use tuple to unify the return format
        else:
            fmt_out = '({},{})'
            coord = self
            pass

        return fmt_out.format(*(format(i, format_spec) for i in coord))


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

    v2 = Vector.frombytes(byte_rep)
    print(v2 == v)

    print(format(v, 'p'))
    print(format(v, '.3ep'))
    print(format(v, '010.5fp'))

    # now the Vector is hashable, and it obey the "hash rule" mentioned above
    print(hash(v))
    print(hash(v2))
