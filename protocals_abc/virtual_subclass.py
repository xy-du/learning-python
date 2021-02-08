# you can register a class as a virtual subclass of an ABC, even if it does not inherit from it.

# 1. When doing so, we promise that the class faithfully implements the
# interface defined in the ABC—and Python will believe us without checking.
# If we lie, we’ll be caught by the usual runtime exceptions.
# 2. The inheritance will not be checked at anytime, not even at runtime
# It’s up to the subclass to ac‐ tually implement all the methods needed to avoid runtime errors.
# 3. issubclass and isinstance work
# 4. it will not inherit any methods or attributes from the ABC.
# 5. The register method is usually invoked as a plain function but it can also be used as a decorator.

from random import randrange

from protocals_abc.define_abc import Tombola


@Tombola.register
class Tomlolist(list):
    load = list.extend

    def pick(self):
        if self:  # it use the __bool__ of list
            position = randrange(len(self))
            return self[position]
        else:
            raise LookupError('pop from empty TomboList')

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tomlolist.register(Tombola)
# for python 3.3 or early, you can not use decorator, so standard call syntax must be used

##############################
# run in python console
##############################
# from protocals_abc.define_abc import Tombola
# from protocals_abc.virtual_subclass import Tomlolist
# issubclass(Tomlolist,Tombola)
# t=Tomlolist()
# isinstance(t,Tombola)
##############################

# NOTE:
# as you can see, the instance of subclass can be seen as the instance
# of ABCs that the subclass registered


# NOTE:
# you can use decorator to register a virtual subclass
# but before python 3.3 you can only use the plain function register()
# to do this, and even this is the 'older' way, it's more widely deployed
# as a function to register classes defined elsewhere.
# see the collections.abc source code
# https://hg.python.org/cpython/file/3.4/Lib/_collections_abc.py
# the built-in types tuple, str, range, and memoryview are registered
# as virtual subclasses of Sequence like this:
#    Sequence.register(tuple)
#    Sequence.register(str)
#    Sequence.register(range)
#    Sequence.register(memoryview)
# So basically, you do the register at the ABCs place, not the place where you define the subclasses
# which is OK because you’ll have to import it anyway to get the ABCs:
# you need access to MutableMapping to be able to write isinstance(my_dict, MutableMapping).
