import abc


# abc.ABC is introduced in Python3.4 and before that, when it's not making sense to sublcass
# another existing ABC, then you must use metadata:
# class Tombola(metaclass=abc.ABCMeta):

# metadata is introduced in python3, before that, you have to use __metaclass__
# class Tombola(object):
#   __metaclass__ = abc.ABCMeta

class Tombola(abc.ABC):  # to define an ABC, inherit abc.ABC
    # abstract method is marked, the body it usually empty.
    # but it can be implemented, and the subclass can use this implementation
    # by super() to add some functions instead of implementing from scratch
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""

    # self.pick() may raise LookupEr ror is also part of its interface,
    # but there is no way to declare this in Python, except in the documentation
    # See the exception hierarchy
    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.
        This method should raise `LookupError` when the instance is empty."""

    # abstract method can include concrete methods
    # concrete method can only rely on the interface defined in ABC (other concrete
    # methods or abstract method or properties of the ABC)
    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.load())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

# because the limitation of the concrete methods in ABC, being aeare of the internal
# data structure, concrete subclass can always overwrite the abstract method for a more
# efficient implementation

# About @abc.abstractmethod
# Besides the @abstractmethod, the abc module defines the @abstractclassmethod,
# @abstractstaticmethod, and @abstractproperty decorators.
# However, these last three are deprecated since Python 3.3,
# when it became possible to stack decorators on top of
# @abstractmethod, making the others redundant.
# eg:
# class MyABC(abc.ABC):
#     @classmethod
#     @abc.abstractmethod
#     def an_abstract_classmethod(cls, ...):
#         pass
# NOTE:
# @abc.abstractmethod should be applied as the innermost decorator

##############################
# run in python console
##############################
# class Fake(Tombola):
#     def pick(self):
#         return 2
#
#
# print(Fake)
# f = Fake()
##############################

# f = Fake() will cause an error:
# TypeError: Can't instantiate abstract class Fake with abstract method load
# since we did inherit the abstract class load, Fake is seen as abstract class
