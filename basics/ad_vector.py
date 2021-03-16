from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)

    def __bool__(self):
        return bool(abs(self))

    def __repr__(self):
        """
        called by repr() build-in.\n
        console, debugger, %r in %-format, !r in format(), they are use this.
        and if this is not exists, they will play something like <Vector Object at 0x10e100070>.
        when __str__ is not available, __repr__ will be called as a fallback.
        why use %r instead of %s, see the example bellow.
        """
        return 'Vector(%r,%r)' % (self.x, self.y)

# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print(v1 + v2)
# print(v1 * 2)
# # this will present an error, since the __mul__ is not implemented in a reversed way which shoul use __rmul__
# # print(2*v1)
# if v1:
#     print('__bool__ test')
#
#
# a = '1'
# b = 2
# print(Vector(a, b))  # output: Vector('1',2). if it's %r used in the __repr__ but %s, output will be Vector(1,2).
# print('%s' % a) #output: 1
# print('%r' % a) #output: '1'
