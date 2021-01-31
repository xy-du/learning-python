# NOT all python object can be the weak reference target, or referent.
# basic list and dict can not be the inferent, but it can be easily worked around by subclass

#   type    original    subclass
#   dict    no          yes
#   list    no          yes
#   set     yes         yes
#   str     no          yes
#   int     no          no
#   tuple   no          no
# this tabulation apply only to CPython, no guarantee for other implementation.


import weakref


class Mylist(list):
    """list subclass whose instances may be weakly referenced"""


a_list = Mylist(range(10))
wrf = weakref.ref(a_list)

# this will cause a TypeError: cannot create weak reference to 'list' object
# b_list = list(range(10))
# wrf_b = weakref.ref(b_list)

# some tricks python plays with immutable
# for tuple, str, bytes, frozenset, the copy made by constructor and [:] is not a new copy, it's the same
# data as it tries to copy from, this is optimization used by CPython.
t1 = (1, 2, 3)
t2 = tuple(t1)
t3 = t1[:]
print(t2 is t1)
print(t3 is t1)
t4 = (1, 2, 3)
print(t4 is t1)

s1 = 'ABC'
s2 = 'ABC'
s3 = str(s1)
print(s1 is s2)
print(s3 is s1)
