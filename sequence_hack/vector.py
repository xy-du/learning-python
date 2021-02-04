import array
import math
import reprlib


class Vector:
    typecode = 'd'

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

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        math.sqrt(sum(i * i for i in self))

    def __bool__(self):
        return bool(abs(self))

    # to make slicing of Vector to return a Vector instance, just simply delegating to array is not working
    def __len__(self):
        return len(self._component)

    def __getitem__(self, item):
        return self._component[item]

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        mem = memoryview(octets[:-1]).cast(typecode)
        return cls(mem)  # no more unpacking here since __init__ accept iterable


if __name__ == '__main__':
    v1 = Vector([3, 4, 5])
    print(len(v1))
    print(v1[-1])
    v2 = Vector(range(10))
    print(v2[1:5])  # return array('d', [1.0, 2.0, 3.0, 4.0]), but returning a Vector would be better
