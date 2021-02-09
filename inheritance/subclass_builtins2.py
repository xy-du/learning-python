# how the problem in subclass_builtins.py can by addressed

# just simply change the dict to UserDict, then all will
# work out just as we expect


# NOTE:
# the problem described applies only to method delegation
# within the C language implementation of the built-in types,
# and only affects userdefined classes derived directly from those types.
# If you subclass from a class coded in Python, such as UserDict or MutableMapping,
# you will not be troubled by this
from collections import UserDict


class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


md = MyDict(one=1)
print(md)
md['two'] = 2
print(md)
md.update(three=3)
print(md)


class MyDict2(UserDict):
    def __getitem__(self, item):
        return 23


mdd = MyDict(one=1)
print(mdd['one'])
d = {}
d.update(mdd)
print(d['one'])
print(d)
