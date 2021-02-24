import keyword
from collections import abc


# We often refer to __init__ as the constructor method, but that’s
# because we adopted jargon from other languages. The special method
# that actually constructs an instance is __new__: it’s a class method
# (but gets special treatment, so the @classmethod decorator
# is not used), and it must return an instance. That instance will in
# turn be passed as the first argument self of __init__. Because __init__
# gets an instance when called, and it’s actually forbidden from returning
# anything, __init__ is really an “initializer.” The real constructor is
# __new__—which we rarely need to code because the implementation inherited
# from object suffices.

# The path just described, from __new__ to __init__, is the most common,
# but not the only one. The __new__ method can also return an instance
# of a different class, and when that happens, the interpreter does not call __init__.

# NOTE:
# FrozenJSON.__new__, when the expression super().__new__(cls) effectively
# calls object.__new__(FrozenJSON), the instance built by the object class
# is actually an instance of FrozenJSON—i.e., the __class__ attribute of the
# new instance will hold a reference to FrozenJSON—even though the actual
# construction is performed by object.__new__, implemented in C, in the
# guts of the interpreter.
class FrozenJSON:
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):  # in case the key is a python keyword, which is invalid
                key += '_'
            elif not str.isidentifier(key):
                pass  # some logic to deal invalid identifier
            self.__data[key] = value

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJSON(self.__data[item])  # KeyError will happen here if item is not in the keys


if __name__ == '__main__':
    from osconfeed import load

    feed = load()
    fj = FrozenJSON(feed)

    print(len(fj.Schedule.speakers))
    print(sorted(fj.Schedule.keys()))
    for key, value in sorted(fj.Schedule.items()):
        print('{:3} {}'.format(len(value), key))

    print(fj.Schedule.speakers[-1].name)
    talk = fj.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
    # print(talk.flavor)  # this one will has a KeyError
