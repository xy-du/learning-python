# apparently, immutable object should never implement in-place special
# methods, since they will be changed 'in-place'

# the in-place operator is more liberal than the infix operator
# for +, we want the two operands are the same type
# but for +=, it's more like update the object in-place, just like
# the list.extend(), and there is no doubt about the type of result


from protocals_abc.define_abc import Tombola
from protocals_abc.subclass_cust_abc import BingoCage


class AddableBingoCage(BingoCage):

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        try:
            other_iterable = iter(other)
            self.load(other_iterable)
            return self
        except TypeError:
            cls_name = type(self).__name__
            msg = 'right operand in += must be {!r} or an iterable'
            raise TypeError(msg.format(cls_name))


if __name__ == '__main__':
    vowels = 'AEIOU'
    globe = AddableBingoCage(vowels)
    print(globe.inspect())
    print(globe.pick() in vowels)
    print(len(globe.inspect()))

    globe2 = AddableBingoCage('XYZ')
    globe3 = globe + globe2
    print(globe3.inspect())

    # TypeError: unsupported operand type(s) for +: 'AddableBingoCage' and 'list'
    # because it use __add__
    # globe4 = globe + ['M', 'N']

    # this is ok because it use __iadd__
    # and __iadd__ works as long as the other args is iterable
    globe3 += ['M', 'N']
    print(globe3.inspect())
