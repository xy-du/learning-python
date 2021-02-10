# you can not overwrite operator for built-in types
# you can not create new operator
# a few operator can not be overload: is, not, or (but the bitwise &, ~, |, can)

# I copy the Vector here for convenience

# here I add __neg__ and __pos__ into the class so that it will support - and + operator

# fundamental rule of operators:
# always return a new object. In other words, do not modify self,
# but create and return a new instance of a suitable type.

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
