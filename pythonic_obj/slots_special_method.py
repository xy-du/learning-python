# Python stores instance attributes in a per-instance dict named __dict__. If you are dealing with millions
# of instances with few attributes, the __slots__ class attribute can save a lot space, by letting the interpreter
# store the instance attribute in a tuple instead of dict

# To define __slots__, you create a class attribute with that name and assign it an iterable of str with identifiers for
# the instance attributes. I like to use a tuple for that, because it conveys the message that the __slots__ definition
# cannot change.
# after this, Python will store the attribute in a tuple-like structure

# NOTE:
#   you will only be able to have the attributes in __slots__, unless you include __dict__ in __slots, which may
# negate the memory saving
#   you have to redeclare __slots__ in the subclass
#   instance can not be target of weak reference unless you remember put the '__weakref__' in __slots__
#   if you are dealing with millions of objects with numeric data, consider using Numpy


from vector_2d import *

v = Vector(1, 2)
v.t = 'test'
print(v.__dict__)


class Vector2():
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


v2 = Vector2(3, 4)


# v2.t = 'test'  # this will cause an error, AttributeError: 'Vector2' object has no attribute 't'
# print(v2.__dict__)  # this will cause an error two


class Vector3():
    __slots__ = ('x', 'y', '__dict__')

    def __init__(self, x, y):
        self.x = x
        self.y = y


v3 = Vector3(5, 6)
v3.t = 'test'  # this will cause an error, AttributeError: 'Vector2' object has no attribute 't'
print(v3.__dict__)  # you only see t in __dict__ because it's a dynamic variable
