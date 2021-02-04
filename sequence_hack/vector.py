import array
import functools
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

    # repr mostly used for debugging, so you don't want a large object to span thousands of lines in you console
    # or log, so here reprelib is used to produce limited-length representation.
    # eg. a list contains millions of number will just be [1,2,3,4,5,...]
    # __repr__ has its role in debugging, so it should never raise a exception
    def __repr__(self):
        cls_name = type(self).__name__  # how to get the class name through the instance of it, here is how
        comp_rep = reprlib.repr(self._component)
        comp_rep = comp_rep[
                   comp_rep.find('['):-1]  # we use the array here, so comp_pre is like array('i',[1,2,3,4,5,...])
        return f'{cls_name}({comp_rep})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._component)

    # # this is not the efficient way if the vector has thousands of component, because it copies all the
    # # content of the vector to make two tuple just to use the __eq__ of tuple
    # def __eq__(self, other):
    #     return tuple(self) == tuple(other)

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(c) for c in self._component)
        return functools.reduce(operator.xor, hashes, 0)  # give reduce an initializer in case the hashes is empty

    def __abs__(self):
        math.sqrt(sum(i * i for i in self))

    def __bool__(self):
        return bool(abs(self))

    # to make slicing of Vector to return a Vector instance, just simply delegating to array is not working
    def __len__(self):
        return len(self._component)

    # def __getitem__(self, item):
    #     return self._component[item]

    def __getitem__(self, item):
        cls = type(self)  # this is how you get class from instance
        if isinstance(item, slice):
            return cls(self._component[item])  # [] accept slice object
        elif isinstance(item, numbers.Integral):  # abstract base class, make an API more flexible and future-proof
            return self._component[item]
        else:
            raise TypeError(f'{cls.__name__} indices must be integers')

    # we want access the first few components with shortcut letters such as x, y, z instead
    # of v[0], v[1] and v[2].
    # The __getattr__ method is invoked by the interpreter when attribute lookup fails.
    # In simple terms, given the expression my_obj.x,
    # Python checks if the my_obj instance has an attribute named x;
    # if not, the search goes to the class (my_obj.__class__),
    # and then up the inheritance graph.
    # If the x attribute is not found,
    # then the __getattr__ method defined in the class of my_obj is called with self and the name of the attribute
    # as a string (e.g., 'x').

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut.find(item)
            if 0 <= pos < len(cls.shortcut):
                return self._component[pos]
        raise AttributeError(f'{cls.__name__!r} has no attribute {item!r}')

    # we don't want the attribute 'a' to 'z' to be set
    # for what it's worth, do not use __slots__ to limit the attribute
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
        return cls(mem)  # no more unpacking here since __init__ accept iterable


if __name__ == '__main__':
    v1 = Vector([3, 4, 5, 6, 7])
    print(len(v1))
    print(v1[-1])
    v2 = Vector(range(10))

    # RUN on python console (so the __repr__ is used instead of __str__ used in print())
    # v2[1:5]  # return array('d', [1.0, 2.0, 3.0, 4.0]), but returning a Vector would be better
    # v2[1:5] # now, it returns Vector([1.0, 2.0, 3.0, 4.0]),
    # print(v2[1:2,4]) # this will cause error because we do not make slicing support multidimensional

    print(v2.y)

    # v2.y = 10  # after customizing the __setattr__, this will raise a exception
    # print(v2.y)
    print(v2)
    # here is the problem, without a proper __setattr__, if you set the value of attribute x/y/z/t, then x will
    # become a attribute of the instance, and the value of instance.x will change from then on even thought the
    # value of the component of the vector has not changed, that is why we need __setattr__

    print(hash(v1))
