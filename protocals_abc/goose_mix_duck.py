from abc import ABCMeta
from collections import abc


class Struggle:
    def __len__(self):
        return 2


print(isinstance(Struggle(), abc.Sized))
print(issubclass(Struggle, abc.Sized))


# both are true, but we do not inherit the Size ABC, the secrete lies
# in the __subclasshook__ method in Size
# the source code of Size:

class Sized(metaclass=ABCMeta):
    __slots__ = ()

    @abc.abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

# The __subclasshook__ adds some duck typing DNA to the whole goose typing proposition.
# You can have formal interface definitions with ABCs,
# you can make isinstance checks everywhere,
# and still have a completely unrelated class play along just
# because it implements a certain method (or because it does whatever
# it takes to convince a __subclasshook__ to vouch for it). Of course,
# this only works for ABCs that do provide a __subclasshook__.

# so this can happen or not is determined by the ABCs, depending on weather and how
# it implement. But the philosophy here is that if you implement a certain method,
# you must implement the way 'I think it is', this assumption is very dangerous, so
# not only we should not create our ABCs as less as possible, even is we did, we may
# not implement __subclasshook__ for the best.
