# see the following two problem

class MyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


md = MyDict(one=1)
print(md)
md['two'] = 2
print(md)
md.update(three=3)
print(md)


# problem here: it violet the OO rule:
# basic rule of object-oriented programming:
# the search for methods should always start from the class of the target instance (self),
# even when the call happens inside a method implemented in a superclass.

class MyDict2(dict):
    def __getitem__(self, item):
        return 23


mdd = MyDict(one=1)
print(mdd['one'])
d = {}
d.update(mdd)
print(d['one'])
print(d)

# here the problem is:
# the overridden methods (__getitem__ here) of other classes should be called by the built-in methods


# in one word:
# the code of the built-ins (written in C, the dict here in this example),
# does not call special methods overridden by user-defined classes.
